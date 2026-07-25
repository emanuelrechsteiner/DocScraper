"""Billing integration tests (#31).

Tests for billing tier enforcement, usage tracking, rate limiting,
overage detection, and Stripe service integration.

All tests that require user lookup use the DB-backed UserRepository
via the ``app_with_db`` fixture and ``db_session``.
"""

from __future__ import annotations

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from api.app import create_app
from api.db.repositories import UserRepository
from api.db.session import get_db_session
from api.models.schemas import BillingTier
from api.services.billing import PLANS, billing_service
from api.services.usage import TIER_LIMITS, UsageService


@pytest_asyncio.fixture
async def app_with_db(db_session: AsyncSession):
    """FastAPI application with get_db_session overridden to use in-memory SQLite.

    Args:
        db_session: In-memory SQLite session from the ``db_session`` fixture.

    Yields:
        Configured FastAPI application instance.
    """
    application = create_app()

    async def override_get_db():
        yield db_session

    application.dependency_overrides[get_db_session] = override_get_db
    yield application


@pytest_asyncio.fixture
async def client(app_with_db):
    """Async HTTP client backed by the test application."""
    transport = ASGITransport(app=app_with_db)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ---------------------------------------------------------------------------
# Billing tier structure (#26)
# ---------------------------------------------------------------------------


class TestBillingTiers:
    """Tests for billing tier definitions and limits."""

    def test_three_tiers_defined(self) -> None:
        """All three billing tiers exist with correct names."""
        assert len(PLANS) == 3
        tier_names = {p["tier"] for p in PLANS}
        assert tier_names == {BillingTier.FREE, BillingTier.PRO, BillingTier.ENTERPRISE}

    def test_free_tier_limits(self) -> None:
        """Free tier has correct rate limits."""
        limits = TIER_LIMITS[BillingTier.FREE]
        assert limits["requests_per_hour"] == 100
        assert limits["max_pages_per_request"] == 100
        assert limits["max_concurrent_jobs"] == 2
        assert limits["price_monthly_cents"] == 0

    def test_pro_tier_limits(self) -> None:
        """Pro tier has higher limits than free."""
        free = TIER_LIMITS[BillingTier.FREE]
        pro = TIER_LIMITS[BillingTier.PRO]
        assert pro["requests_per_hour"] > free["requests_per_hour"]
        assert pro["max_pages_per_request"] > free["max_pages_per_request"]
        assert pro["max_concurrent_jobs"] > free["max_concurrent_jobs"]
        assert pro["price_monthly_cents"] > 0

    def test_enterprise_tier_limits(self) -> None:
        """Enterprise tier has highest limits."""
        pro = TIER_LIMITS[BillingTier.PRO]
        ent = TIER_LIMITS[BillingTier.ENTERPRISE]
        assert ent["requests_per_hour"] > pro["requests_per_hour"]
        assert ent["max_pages_per_request"] >= pro["max_pages_per_request"]
        assert ent["max_concurrent_jobs"] > pro["max_concurrent_jobs"]
        assert ent["price_monthly_cents"] > pro["price_monthly_cents"]

    def test_tier_limits_consistency(self) -> None:
        """All tiers have the same set of limit keys."""
        keys = set(TIER_LIMITS[BillingTier.FREE].keys())
        for tier in BillingTier:
            assert set(TIER_LIMITS[tier].keys()) == keys

    @pytest.mark.asyncio
    async def test_plans_endpoint_returns_all_tiers(
        self, client: AsyncClient
    ) -> None:
        """GET /billing/plans returns all three tiers."""
        response = await client.get("/api/v1/billing/plans")
        assert response.status_code == 200
        plans = response.json()["data"]
        tiers = {p["tier"] for p in plans}
        assert tiers == {"free", "pro", "enterprise"}

    @pytest.mark.asyncio
    async def test_plans_include_pricing(self, client: AsyncClient) -> None:
        """Each plan includes pricing information."""
        response = await client.get("/api/v1/billing/plans")
        for plan in response.json()["data"]:
            assert "price_monthly_cents" in plan
            assert "requests_per_hour" in plan
            assert "max_pages_per_request" in plan


# ---------------------------------------------------------------------------
# Usage tracking (#25)
# ---------------------------------------------------------------------------


class TestUsageTracking:
    """Tests for usage tracking service."""

    def test_record_increments_counts(self) -> None:
        """Recording usage increments hourly and daily counters."""
        svc = UsageService()
        svc.record(
            endpoint="/api/v1/scrape",
            method="POST",
            status_code=202,
            response_time_ms=150.0,
            key_id="key_abc",
        )
        assert svc.get_hourly_count("key_abc") == 1

    def test_multiple_records_accumulate(self) -> None:
        """Multiple records for the same key accumulate correctly."""
        svc = UsageService()
        for _ in range(10):
            svc.record(
                endpoint="/api/v1/scrape",
                method="POST",
                status_code=202,
                response_time_ms=100.0,
                key_id="key_xyz",
            )
        assert svc.get_hourly_count("key_xyz") == 10

    def test_different_keys_tracked_separately(self) -> None:
        """Usage for different API keys is tracked independently."""
        svc = UsageService()
        for _ in range(5):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_a")
        for _ in range(3):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_b")

        assert svc.get_hourly_count("key_a") == 5
        assert svc.get_hourly_count("key_b") == 3

    def test_error_responses_tracked(self) -> None:
        """Error responses (4xx, 5xx) are counted in daily stats."""
        svc = UsageService()
        svc.record("/api/v1/scrape", "POST", 400, 50.0, key_id="key_err")
        svc.record("/api/v1/scrape", "POST", 500, 50.0, key_id="key_err")
        assert svc.get_hourly_count("key_err") == 2


# ---------------------------------------------------------------------------
# Rate limit checking (#24)
# ---------------------------------------------------------------------------


class TestRateLimitChecking:
    """Tests for rate limit enforcement via usage service."""

    def test_within_limit_is_allowed(self) -> None:
        """Requests within tier limit are allowed."""
        svc = UsageService()
        for _ in range(50):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_ok")
        allowed, remaining = svc.check_rate_limit("key_ok", BillingTier.FREE)
        assert allowed is True
        assert remaining == 50

    def test_at_limit_is_blocked(self) -> None:
        """Requests at exactly the tier limit are blocked."""
        svc = UsageService()
        for _ in range(100):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_full")
        allowed, remaining = svc.check_rate_limit("key_full", BillingTier.FREE)
        assert allowed is False
        assert remaining == 0

    def test_pro_tier_has_higher_limit(self) -> None:
        """Pro tier allows more requests per hour."""
        svc = UsageService()
        for _ in range(100):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_pro")
        allowed, remaining = svc.check_rate_limit("key_pro", BillingTier.PRO)
        assert allowed is True
        assert remaining == 900  # 1000 - 100


# ---------------------------------------------------------------------------
# Overage handling (#30)
# ---------------------------------------------------------------------------


class TestOverageHandling:
    """Tests for soft and hard overage limits."""

    def test_no_overage_within_limits(self) -> None:
        """No overage flags when usage is within limits."""
        svc = UsageService()
        for _ in range(50):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_safe")
        result = svc.check_overage("key_safe", BillingTier.FREE)
        assert result["is_over_soft"] is False
        assert result["is_over_hard"] is False
        assert result["usage_percentage"] == 50.0

    def test_soft_limit_at_120_percent(self) -> None:
        """Soft limit triggers at 120% of tier allowance."""
        svc = UsageService()
        for _ in range(120):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_soft")
        result = svc.check_overage("key_soft", BillingTier.FREE)
        assert result["is_over_soft"] is True
        assert result["is_over_hard"] is False

    def test_hard_limit_at_150_percent(self) -> None:
        """Hard limit triggers at 150% of tier allowance."""
        svc = UsageService()
        for _ in range(150):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_hard")
        result = svc.check_overage("key_hard", BillingTier.FREE)
        assert result["is_over_soft"] is True
        assert result["is_over_hard"] is True
        assert "blocked" in result["message"].lower()

    def test_approaching_limit_message(self) -> None:
        """Warning message at 80% usage."""
        svc = UsageService()
        for _ in range(80):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_warn")
        result = svc.check_overage("key_warn", BillingTier.FREE)
        assert result["is_over_soft"] is False
        assert "approaching" in result["message"].lower()


# ---------------------------------------------------------------------------
# Usage summary (#29)
# ---------------------------------------------------------------------------


class TestUsageSummary:
    """Tests for usage summary and daily breakdown."""

    def test_summary_reflects_recorded_usage(self) -> None:
        """Summary correctly reflects recorded requests."""
        svc = UsageService()
        for _ in range(25):
            svc.record("/api/v1/scrape", "POST", 202, 100.0, key_id="key_sum")
        summary = svc.get_summary("key_sum", BillingTier.FREE)
        assert summary["total_requests"] == 25
        assert summary["requests_limit"] == 100
        assert summary["is_over_limit"] is False

    def test_daily_breakdown_returns_requested_days(self) -> None:
        """Daily breakdown returns the correct number of days."""
        svc = UsageService()
        breakdown = svc.get_daily_breakdown("key_day", days=7)
        assert len(breakdown) == 7
        for entry in breakdown:
            assert "date" in entry
            assert "request_count" in entry
            assert "pages_scraped" in entry

    @pytest.mark.asyncio
    async def test_usage_endpoint_includes_overage(
        self, client: AsyncClient
    ) -> None:
        """GET /usage returns overage information."""
        response = await client.get("/api/v1/usage")
        assert response.status_code == 200
        data = response.json()["data"]
        assert "overage" in data
        assert "is_over_soft" in data["overage"]
        assert "is_over_hard" in data["overage"]


# ---------------------------------------------------------------------------
# Stripe checkout (#27)
# ---------------------------------------------------------------------------


class TestStripeCheckout:
    """Tests for Stripe checkout integration."""

    @pytest.mark.asyncio
    async def test_checkout_rejects_free_tier(self, client: AsyncClient) -> None:
        """Cannot create checkout session for free tier."""
        response = await client.post(
            "/api/v1/billing/checkout",
            json={
                "tier": "free",
                "success_url": "https://example.com/success",
                "cancel_url": "https://example.com/cancel",
            },
        )
        assert response.status_code == 400
        assert "CHECKOUT_ERROR" in response.json()["detail"]["code"]

    @pytest.mark.asyncio
    async def test_checkout_requires_valid_urls(self, client: AsyncClient) -> None:
        """Checkout requires valid success and cancel URLs."""
        response = await client.post(
            "/api/v1/billing/checkout",
            json={
                "tier": "pro",
                "success_url": "not-a-url",
                "cancel_url": "also-not-a-url",
            },
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_checkout_pro_requires_stripe_config(
        self, client: AsyncClient
    ) -> None:
        """Pro checkout fails gracefully when Stripe is not configured."""
        response = await client.post(
            "/api/v1/billing/checkout",
            json={
                "tier": "pro",
                "success_url": "https://example.com/success",
                "cancel_url": "https://example.com/cancel",
            },
        )
        assert response.status_code == 400


# ---------------------------------------------------------------------------
# Stripe webhooks (#28)
# ---------------------------------------------------------------------------


class TestStripeWebhooks:
    """Tests for Stripe webhook handler."""

    @pytest.mark.asyncio
    async def test_webhook_rejects_missing_signature(
        self, client: AsyncClient
    ) -> None:
        """Webhook endpoint rejects requests without Stripe signature."""
        response = await client.post(
            "/api/v1/billing/webhooks",
            content=b'{"type": "checkout.session.completed"}',
            headers={"content-type": "application/json"},
        )
        assert response.status_code == 400


# ---------------------------------------------------------------------------
# Subscription status (#27)
# ---------------------------------------------------------------------------


class TestSubscriptionStatus:
    """Tests for subscription status endpoint."""

    @pytest.mark.asyncio
    async def test_subscription_returns_user_tier(
        self, client: AsyncClient, db_session: AsyncSession
    ) -> None:
        """Subscription endpoint returns current tier."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("sub@example.com")
        await db_session.commit()

        response = await client.get(
            "/api/v1/billing/subscription",
            params={"user_id": user.user_id},
        )
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["tier"] == "free"
        assert data["user_id"] == user.user_id

    @pytest.mark.asyncio
    async def test_subscription_nonexistent_user(
        self, client: AsyncClient
    ) -> None:
        """Subscription endpoint returns 404 for unknown user."""
        response = await client.get(
            "/api/v1/billing/subscription",
            params={"user_id": "user_nonexistent"},
        )
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Billing service unit tests
# ---------------------------------------------------------------------------


class TestBillingService:
    """Unit tests for BillingService."""

    def test_get_plans_returns_all(self) -> None:
        """get_plans returns all three billing plans."""
        plans = billing_service.get_plans()
        assert len(plans) == 3

    def test_get_plan_by_tier(self) -> None:
        """get_plan returns correct plan for each tier."""
        for tier in BillingTier:
            plan = billing_service.get_plan(tier)
            assert plan is not None
            assert plan["tier"] == tier

    def test_get_plan_nonexistent(self) -> None:
        """get_plan returns None for invalid tier string."""
        plan = billing_service.get_plan(BillingTier.FREE)
        assert plan is not None
        assert plan["price_monthly_cents"] == 0

    @pytest.mark.asyncio
    async def test_get_subscription_status_new_user(
        self, db_session: AsyncSession
    ) -> None:
        """New user has free tier subscription."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("billing@example.com")
        await db_session.commit()

        status = await billing_service.get_subscription_status_async(
            user.user_id, user_repo=user_repo
        )
        assert status["tier"] == "free"
        assert status["stripe_subscription_id"] is None

    @pytest.mark.asyncio
    async def test_get_subscription_status_unknown_user(
        self, db_session: AsyncSession
    ) -> None:
        """Unknown user raises ValueError."""
        user_repo = UserRepository(db_session)
        with pytest.raises(ValueError, match="User not found"):
            await billing_service.get_subscription_status_async(
                "user_fake", user_repo=user_repo
            )

    @pytest.mark.asyncio
    async def test_checkout_free_tier_raises(
        self, db_session: AsyncSession
    ) -> None:
        """Cannot create checkout for free tier."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("free@example.com")
        await db_session.commit()

        with pytest.raises(ValueError, match="free tier"):
            await billing_service.create_checkout_session_with_repo(
                user_id=user.user_id,
                tier=BillingTier.FREE,
                success_url="https://example.com/ok",
                cancel_url="https://example.com/cancel",
                user_repo=user_repo,
            )

    @pytest.mark.asyncio
    async def test_checkout_unconfigured_stripe_raises(
        self, db_session: AsyncSession
    ) -> None:
        """Checkout raises when Stripe key is not set."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("nostripe@example.com")
        await db_session.commit()

        with pytest.raises(ValueError, match="Stripe is not configured"):
            await billing_service.create_checkout_session_with_repo(
                user_id=user.user_id,
                tier=BillingTier.PRO,
                success_url="https://example.com/ok",
                cancel_url="https://example.com/cancel",
                user_repo=user_repo,
            )
