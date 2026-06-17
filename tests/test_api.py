"""API integration tests (#23).

Tests for all Parsify REST API endpoints using httpx AsyncClient.
Covers: scrape, jobs, process, auth, billing plans, usage.

All tests use an in-memory SQLite database via the ``app_with_db`` fixture,
which overrides the ``get_db_session`` dependency.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from api.app import create_app
from api.db.repositories import JobRepository, UserRepository, APIKeyRepository
from api.db.session import get_db_session
from api.models.schemas import JobStatus


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
    """Async HTTP client backed by the test application.

    Args:
        app_with_db: Application with DB session override.

    Yields:
        Configured ``AsyncClient`` instance.
    """
    transport = ASGITransport(app=app_with_db)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------


class TestHealthCheck:
    """Tests for GET /health."""

    @pytest.mark.asyncio
    async def test_health_returns_200(self, client: AsyncClient) -> None:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


# ---------------------------------------------------------------------------
# Scrape endpoint (#15)
# ---------------------------------------------------------------------------


class TestScrapeEndpoint:
    """Tests for POST /api/v1/scrape."""

    @pytest.mark.asyncio
    async def test_create_scrape_job(self, client: AsyncClient) -> None:
        """Submitting a scrape request returns 202 with a job ID."""
        response = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com", "max_pages": 10},
        )
        assert response.status_code == 202
        body = response.json()
        assert body["data"]["job_id"].startswith("job_")
        assert body["data"]["status"] == "pending"
        assert body["meta"]["request_id"].startswith("req_")

    @pytest.mark.asyncio
    async def test_scrape_invalid_url(self, client: AsyncClient) -> None:
        """Invalid URL returns 422 validation error."""
        response = await client.post(
            "/api/v1/scrape",
            json={"url": "not-a-url"},
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_scrape_max_pages_validation(self, client: AsyncClient) -> None:
        """max_pages must be between 1 and 10000."""
        response = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com", "max_pages": 0},
        )
        assert response.status_code == 422

        response = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com", "max_pages": 99999},
        )
        assert response.status_code == 422


# ---------------------------------------------------------------------------
# Job status/result endpoints (#16, #17)
# ---------------------------------------------------------------------------


class TestJobEndpoints:
    """Tests for GET /api/v1/jobs endpoints."""

    @pytest.mark.asyncio
    async def test_get_job_status(self, client: AsyncClient) -> None:
        """Created job is retrievable by ID."""
        create_resp = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com"},
        )
        job_id = create_resp.json()["data"]["job_id"]

        response = await client.get(f"/api/v1/jobs/{job_id}")
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["job_id"] == job_id
        assert data["status"] == "pending"

    @pytest.mark.asyncio
    async def test_get_job_not_found(self, client: AsyncClient) -> None:
        """Non-existent job returns 404."""
        response = await client.get("/api/v1/jobs/job_nonexistent")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_job_result_not_complete(self, client: AsyncClient) -> None:
        """Requesting result of pending job returns 409."""
        create_resp = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com"},
        )
        job_id = create_resp.json()["data"]["job_id"]

        response = await client.get(f"/api/v1/jobs/{job_id}/result")
        assert response.status_code == 409

    @pytest.mark.asyncio
    async def test_get_job_result_completed(
        self, client: AsyncClient, db_session: AsyncSession
    ) -> None:
        """Completed job result is retrievable."""
        create_resp = await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com"},
        )
        job_id = create_resp.json()["data"]["job_id"]

        # Manually complete the job via repository
        repo = JobRepository(db_session)
        await repo.update(
            job_id,
            status=JobStatus.COMPLETED.value,
            completed_at=datetime.now(timezone.utc),
            pages_scraped=5,
            output_files=["page1.md", "page2.md"],
            summary={"total": 5},
        )
        await db_session.commit()

        response = await client.get(f"/api/v1/jobs/{job_id}/result")
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["total_pages"] == 5
        assert len(data["output_files"]) == 2

    @pytest.mark.asyncio
    async def test_list_jobs(self, client: AsyncClient) -> None:
        """List endpoint returns all created jobs."""
        await client.post(
            "/api/v1/scrape",
            json={"url": "https://docs.example.com"},
        )
        await client.post(
            "/api/v1/scrape",
            json={"url": "https://other.example.com"},
        )

        response = await client.get("/api/v1/jobs")
        assert response.status_code == 200
        body = response.json()
        assert len(body["data"]) == 2
        assert body["meta"]["total"] == 2


# ---------------------------------------------------------------------------
# Process endpoint (#18)
# ---------------------------------------------------------------------------


class TestProcessEndpoint:
    """Tests for POST /api/v1/process."""

    @pytest.mark.asyncio
    async def test_create_process_job(self, client: AsyncClient) -> None:
        """Submitting a process request returns 202."""
        response = await client.post(
            "/api/v1/process",
            json={"input_dir": "/tmp/scraped_docs"},
        )
        assert response.status_code == 202
        body = response.json()
        assert body["data"]["job_id"].startswith("job_")
        assert body["data"]["status"] == "pending"


# ---------------------------------------------------------------------------
# Auth endpoints (#20, #21)
# ---------------------------------------------------------------------------


class TestAuthEndpoints:
    """Tests for /api/v1/auth endpoints."""

    @pytest.mark.asyncio
    async def test_register_user(self, client: AsyncClient) -> None:
        """User registration returns 201 with user ID."""
        response = await client.post(
            "/api/v1/auth/register",
            json={"email": "test@example.com", "name": "Test User"},
        )
        assert response.status_code == 201
        data = response.json()["data"]
        assert data["user_id"].startswith("user_")
        assert data["email"] == "test@example.com"
        assert data["tier"] == "free"

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client: AsyncClient) -> None:
        """Duplicate email returns 409."""
        await client.post(
            "/api/v1/auth/register",
            json={"email": "dupe@example.com"},
        )
        response = await client.post(
            "/api/v1/auth/register",
            json={"email": "dupe@example.com"},
        )
        assert response.status_code == 409

    @pytest.mark.asyncio
    async def test_create_and_list_api_keys(self, client: AsyncClient) -> None:
        """Create a key and verify it appears in the list."""
        reg_resp = await client.post(
            "/api/v1/auth/register",
            json={"email": "keys@example.com"},
        )
        user_id = reg_resp.json()["data"]["user_id"]

        create_resp = await client.post(
            "/api/v1/auth/keys",
            json={"name": "Test Key"},
            params={"user_id": user_id},
        )
        assert create_resp.status_code == 201
        key_data = create_resp.json()["data"]
        assert key_data["key"].startswith("pk_")
        assert key_data["name"] == "Test Key"

        list_resp = await client.get(
            "/api/v1/auth/keys",
            params={"user_id": user_id},
        )
        assert list_resp.status_code == 200
        keys = list_resp.json()["data"]["keys"]
        assert len(keys) == 1
        assert keys[0]["key"] is None  # Full key not exposed in list

    @pytest.mark.asyncio
    async def test_revoke_api_key(self, client: AsyncClient) -> None:
        """Revoked key is deactivated."""
        reg_resp = await client.post(
            "/api/v1/auth/register",
            json={"email": "revoke@example.com"},
        )
        user_id = reg_resp.json()["data"]["user_id"]

        create_resp = await client.post(
            "/api/v1/auth/keys",
            json={"name": "Revoke Me"},
            params={"user_id": user_id},
        )
        key_id = create_resp.json()["data"]["key_id"]

        del_resp = await client.delete(
            f"/api/v1/auth/keys/{key_id}",
            params={"user_id": user_id},
        )
        assert del_resp.status_code == 200


# ---------------------------------------------------------------------------
# Billing endpoints (#26, #27)
# ---------------------------------------------------------------------------


class TestBillingEndpoints:
    """Tests for /api/v1/billing endpoints."""

    @pytest.mark.asyncio
    async def test_list_plans(self, client: AsyncClient) -> None:
        """Plans endpoint returns all three tiers."""
        response = await client.get("/api/v1/billing/plans")
        assert response.status_code == 200
        plans = response.json()["data"]
        assert len(plans) == 3
        tiers = {p["tier"] for p in plans}
        assert tiers == {"free", "pro", "enterprise"}

    @pytest.mark.asyncio
    async def test_checkout_free_tier_rejected(self, client: AsyncClient) -> None:
        """Cannot create checkout for free tier."""
        response = await client.post(
            "/api/v1/billing/checkout",
            json={
                "tier": "free",
                "success_url": "https://example.com/success",
                "cancel_url": "https://example.com/cancel",
            },
        )
        assert response.status_code == 400


# ---------------------------------------------------------------------------
# Usage endpoints (#29)
# ---------------------------------------------------------------------------


class TestUsageEndpoints:
    """Tests for /api/v1/usage endpoints."""

    @pytest.mark.asyncio
    async def test_get_usage_summary(self, client: AsyncClient) -> None:
        """Usage summary returns usage data."""
        response = await client.get("/api/v1/usage")
        assert response.status_code == 200
        data = response.json()["data"]
        assert "total_requests" in data
        assert "overage" in data

    @pytest.mark.asyncio
    async def test_get_daily_usage(self, client: AsyncClient) -> None:
        """Daily usage returns list of daily entries."""
        response = await client.get("/api/v1/usage/daily", params={"days": 7})
        assert response.status_code == 200
        data = response.json()["data"]
        assert isinstance(data, list)
        assert len(data) == 7


# ---------------------------------------------------------------------------
# API key verification (repository integration, #20)
# ---------------------------------------------------------------------------


class TestAPIKeyAuth:
    """Tests for API key authentication via repository."""

    @pytest.mark.asyncio
    async def test_valid_api_key_verification(
        self, db_session: AsyncSession
    ) -> None:
        """APIKeyRepository correctly verifies a valid key."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("auth@example.com")
        await db_session.commit()

        key_repo = APIKeyRepository(db_session)
        key_data, raw_key = await key_repo.create(user.user_id, "test")
        await db_session.commit()

        verified = await key_repo.verify(raw_key)
        assert verified is not None
        assert verified.key_id == key_data.key_id

    @pytest.mark.asyncio
    async def test_invalid_api_key_rejected(
        self, db_session: AsyncSession
    ) -> None:
        """Invalid key returns None."""
        key_repo = APIKeyRepository(db_session)
        verified = await key_repo.verify("pk_invalid_key_12345")
        assert verified is None

    @pytest.mark.asyncio
    async def test_revoked_key_rejected(
        self, db_session: AsyncSession
    ) -> None:
        """Revoked key returns None on verification."""
        user_repo = UserRepository(db_session)
        user = await user_repo.create("revoked@example.com")
        await db_session.commit()

        key_repo = APIKeyRepository(db_session)
        key_data, raw_key = await key_repo.create(user.user_id, "revoke-test")
        await db_session.commit()

        await key_repo.revoke(key_data.key_id, user.user_id)
        await db_session.commit()

        verified = await key_repo.verify(raw_key)
        assert verified is None


# ---------------------------------------------------------------------------
# Usage service logic (#25, #30)
# ---------------------------------------------------------------------------


class TestUsageService:
    """Tests for usage tracking and overage detection (in-memory service)."""

    @pytest.mark.asyncio
    async def test_record_and_check_usage(self) -> None:
        """Usage is tracked and rate limits are enforced."""
        from api.models.schemas import BillingTier
        from api.services.usage import UsageService

        svc = UsageService()
        for _ in range(5):
            svc.record(
                endpoint="/api/v1/scrape",
                method="POST",
                status_code=202,
                response_time_ms=100.0,
                key_id="test_key",
            )

        allowed, remaining = svc.check_rate_limit("test_key", BillingTier.FREE)
        assert allowed is True
        assert remaining == 95  # 100 - 5

    @pytest.mark.asyncio
    async def test_overage_detection(self) -> None:
        """Overage is detected when usage exceeds soft limit."""
        from api.models.schemas import BillingTier
        from api.services.usage import UsageService

        svc = UsageService()
        for _ in range(125):
            svc.record(
                endpoint="/api/v1/scrape",
                method="POST",
                status_code=202,
                response_time_ms=50.0,
                key_id="heavy_user",
            )

        overage = svc.check_overage("heavy_user", BillingTier.FREE)
        assert overage["is_over_soft"] is True
        assert overage["is_over_hard"] is False
        assert overage["usage_percentage"] == 125.0
