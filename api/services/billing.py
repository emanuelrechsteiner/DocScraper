"""Stripe billing service (#26, #27, #28).

Handles subscription checkout, webhook processing, and plan management.
See ADR-006 for design rationale.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from ..config import settings
from ..models.schemas import BillingTier
from .auth_service import auth_service
from .usage import TIER_LIMITS

if TYPE_CHECKING:
    from ..db.repositories import UserRepository

logger = logging.getLogger(__name__)


# Billing plan definitions (#26)
PLANS: list[dict[str, Any]] = [
    {
        "tier": BillingTier.FREE,
        "name": "Free",
        "description": "For evaluation and small projects",
        **TIER_LIMITS[BillingTier.FREE],
    },
    {
        "tier": BillingTier.PRO,
        "name": "Pro",
        "description": "For production workloads",
        **TIER_LIMITS[BillingTier.PRO],
    },
    {
        "tier": BillingTier.ENTERPRISE,
        "name": "Enterprise",
        "description": "For high-volume and enterprise use",
        **TIER_LIMITS[BillingTier.ENTERPRISE],
    },
]


class BillingService:
    """Manages Stripe subscriptions and billing tier transitions."""

    def __init__(self) -> None:
        self._stripe: Any = None

    def _get_stripe(self) -> Any:
        """Lazy-load Stripe SDK to avoid import errors when key is empty."""
        if self._stripe is None:
            import stripe

            stripe.api_key = settings.stripe_secret_key
            self._stripe = stripe
        return self._stripe

    def get_plans(self) -> list[dict[str, Any]]:
        """Return all available billing plans."""
        return PLANS

    def get_plan(self, tier: BillingTier) -> dict[str, Any] | None:
        """Return a specific billing plan."""
        for plan in PLANS:
            if plan["tier"] == tier:
                return plan
        return None

    # ------------------------------------------------------------------
    # In-memory versions (kept for backward compatibility)
    # ------------------------------------------------------------------

    async def create_checkout_session(
        self,
        user_id: str,
        tier: BillingTier,
        success_url: str,
        cancel_url: str,
    ) -> dict[str, str]:
        """Create a Stripe Checkout session (in-memory user lookup).

        Args:
            user_id: The user upgrading.
            tier: Target billing tier.
            success_url: Redirect URL on successful payment.
            cancel_url: Redirect URL on cancellation.

        Returns:
            Dict with checkout_url and session_id.

        Raises:
            ValueError: If tier is FREE or Stripe is not configured.
        """
        if tier == BillingTier.FREE:
            raise ValueError("Cannot create checkout for free tier")

        if not settings.stripe_secret_key:
            raise ValueError(
                "Stripe is not configured. Set PARSIFY_STRIPE_SECRET_KEY."
            )

        stripe = self._get_stripe()

        user = auth_service.get_user(user_id)
        if user is None:
            raise ValueError(f"User not found: {user_id}")

        customer_id = user.stripe_customer_id
        if customer_id is None:
            customer = stripe.Customer.create(
                email=user.email,
                metadata={"parsify_user_id": user_id},
            )
            customer_id = customer.id
            auth_service.update_user(user_id, stripe_customer_id=customer_id)

        price_map = {
            BillingTier.PRO: settings.stripe_price_pro,
            BillingTier.ENTERPRISE: settings.stripe_price_enterprise,
        }
        price_id = price_map.get(tier)
        if not price_id:
            raise ValueError(f"No Stripe price configured for tier: {tier}")

        session = stripe.checkout.Session.create(
            customer=customer_id,
            mode="subscription",
            line_items=[{"price": price_id, "quantity": 1}],
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={"parsify_user_id": user_id, "tier": tier.value},
        )

        logger.info(
            "Created Stripe checkout session %s for user %s (tier: %s)",
            session.id,
            user_id,
            tier.value,
        )
        return {"checkout_url": session.url, "session_id": session.id}

    async def handle_webhook_event(
        self, payload: bytes, signature: str
    ) -> dict[str, str]:
        """Process a Stripe webhook event (in-memory user lookup, #28).

        Args:
            payload: Raw request body bytes.
            signature: Stripe-Signature header value.

        Returns:
            Dict with event type and handling result.

        Raises:
            ValueError: If signature verification fails.
        """
        stripe = self._get_stripe()

        if not settings.stripe_webhook_secret:
            raise ValueError("Stripe webhook secret not configured")

        event = stripe.Webhook.construct_event(
            payload, signature, settings.stripe_webhook_secret
        )

        event_type = event["type"]
        logger.info("Processing Stripe webhook: %s", event_type)

        if event_type == "checkout.session.completed":
            await self._handle_checkout_completed(event["data"]["object"])
        elif event_type == "customer.subscription.updated":
            await self._handle_subscription_updated(event["data"]["object"])
        elif event_type == "customer.subscription.deleted":
            await self._handle_subscription_deleted(event["data"]["object"])
        elif event_type == "invoice.payment_failed":
            await self._handle_payment_failed(event["data"]["object"])
        else:
            logger.debug("Unhandled Stripe event: %s", event_type)

        return {"event_type": event_type, "status": "processed"}

    async def _handle_checkout_completed(self, session: dict[str, Any]) -> None:
        """Activate subscription after successful checkout."""
        user_id = session.get("metadata", {}).get("parsify_user_id")
        tier_str = session.get("metadata", {}).get("tier")
        subscription_id = session.get("subscription")

        if user_id and tier_str:
            tier = BillingTier(tier_str)
            auth_service.update_user(
                user_id,
                tier=tier,
                stripe_subscription_id=subscription_id,
            )
            logger.info("Activated %s tier for user %s", tier.value, user_id)

    async def _handle_subscription_updated(
        self, subscription: dict[str, Any]
    ) -> None:
        """Handle subscription changes (upgrades/downgrades)."""
        customer_id = subscription.get("customer")
        status = subscription.get("status")
        logger.info(
            "Subscription updated for customer %s: status=%s",
            customer_id,
            status,
        )

    async def _handle_subscription_deleted(
        self, subscription: dict[str, Any]
    ) -> None:
        """Downgrade user to free tier when subscription is cancelled."""
        customer_id = subscription.get("customer")
        for user in auth_service._users.values():
            if user.stripe_customer_id == customer_id:
                user.tier = BillingTier.FREE
                user.stripe_subscription_id = None
                logger.info("Downgraded user %s to free tier", user.user_id)
                break

    async def _handle_payment_failed(self, invoice: dict[str, Any]) -> None:
        """Log payment failure for monitoring."""
        customer_id = invoice.get("customer")
        logger.warning("Payment failed for customer %s", customer_id)

    def get_subscription_status(self, user_id: str) -> dict[str, Any]:
        """Get the current subscription status for a user (in-memory lookup)."""
        user = auth_service.get_user(user_id)
        if user is None:
            raise ValueError(f"User not found: {user_id}")

        return {
            "user_id": user_id,
            "tier": user.tier.value,
            "stripe_subscription_id": user.stripe_subscription_id,
            "is_active": (
                user.tier != BillingTier.FREE or user.stripe_subscription_id is None
            ),
        }

    # ------------------------------------------------------------------
    # DB-backed versions (used by routers from Phase 3 onward)
    # ------------------------------------------------------------------

    async def create_checkout_session_with_repo(
        self,
        user_id: str,
        tier: BillingTier,
        success_url: str,
        cancel_url: str,
        user_repo: UserRepository,
    ) -> dict[str, str]:
        """Create a Stripe Checkout session using a DB-backed user repository.

        Args:
            user_id: The user upgrading.
            tier: Target billing tier.
            success_url: Redirect URL on successful payment.
            cancel_url: Redirect URL on cancellation.
            user_repo: Database-backed ``UserRepository`` for this request.

        Returns:
            Dict with checkout_url and session_id.

        Raises:
            ValueError: If tier is FREE or Stripe is not configured.
        """
        if tier == BillingTier.FREE:
            raise ValueError("Cannot create checkout for free tier")

        if not settings.stripe_secret_key:
            raise ValueError(
                "Stripe is not configured. Set PARSIFY_STRIPE_SECRET_KEY."
            )

        stripe = self._get_stripe()

        user = await user_repo.get_by_user_id(user_id)
        if user is None:
            raise ValueError(f"User not found: {user_id}")

        customer_id = user.stripe_customer_id
        if customer_id is None:
            customer = stripe.Customer.create(
                email=user.email,
                metadata={"parsify_user_id": user_id},
            )
            customer_id = customer.id
            await user_repo.update(user_id, stripe_customer_id=customer_id)

        price_map = {
            BillingTier.PRO: settings.stripe_price_pro,
            BillingTier.ENTERPRISE: settings.stripe_price_enterprise,
        }
        price_id = price_map.get(tier)
        if not price_id:
            raise ValueError(f"No Stripe price configured for tier: {tier}")

        session = stripe.checkout.Session.create(
            customer=customer_id,
            mode="subscription",
            line_items=[{"price": price_id, "quantity": 1}],
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={"parsify_user_id": user_id, "tier": tier.value},
        )

        logger.info(
            "Created Stripe checkout session %s for user %s (tier: %s)",
            session.id,
            user_id,
            tier.value,
        )
        return {"checkout_url": session.url, "session_id": session.id}

    async def handle_webhook_event_with_repo(
        self,
        payload: bytes,
        signature: str,
        user_repo: UserRepository,
    ) -> dict[str, str]:
        """Process a Stripe webhook event using a DB-backed user repository (#28).

        Args:
            payload: Raw request body bytes.
            signature: Stripe-Signature header value.
            user_repo: Database-backed ``UserRepository`` for this request.

        Returns:
            Dict with event type and handling result.

        Raises:
            ValueError: If signature verification fails.
        """
        stripe = self._get_stripe()

        if not settings.stripe_webhook_secret:
            raise ValueError("Stripe webhook secret not configured")

        event = stripe.Webhook.construct_event(
            payload, signature, settings.stripe_webhook_secret
        )

        event_type = event["type"]
        logger.info("Processing Stripe webhook: %s", event_type)

        if event_type == "checkout.session.completed":
            await self._handle_checkout_completed_db(
                event["data"]["object"], user_repo
            )
        elif event_type == "customer.subscription.updated":
            await self._handle_subscription_updated(event["data"]["object"])
        elif event_type == "customer.subscription.deleted":
            await self._handle_subscription_deleted_db(
                event["data"]["object"], user_repo
            )
        elif event_type == "invoice.payment_failed":
            await self._handle_payment_failed(event["data"]["object"])
        else:
            logger.debug("Unhandled Stripe event: %s", event_type)

        return {"event_type": event_type, "status": "processed"}

    async def _handle_checkout_completed_db(
        self,
        session: dict[str, Any],
        user_repo: UserRepository,
    ) -> None:
        """Activate subscription after successful checkout (DB-backed)."""
        user_id = session.get("metadata", {}).get("parsify_user_id")
        tier_str = session.get("metadata", {}).get("tier")
        subscription_id = session.get("subscription")

        if user_id and tier_str:
            tier = BillingTier(tier_str)
            await user_repo.update(
                user_id,
                tier=tier.value,
                stripe_subscription_id=subscription_id,
            )
            logger.info("Activated %s tier for user %s", tier.value, user_id)

    async def _handle_subscription_deleted_db(
        self,
        subscription: dict[str, Any],
        user_repo: UserRepository,
    ) -> None:
        """Downgrade user to free tier when subscription is cancelled (DB-backed)."""
        customer_id = subscription.get("customer")
        if customer_id:
            user = await user_repo.get_by_stripe_customer_id(customer_id)
            if user:
                await user_repo.update(
                    user.user_id,
                    tier=BillingTier.FREE.value,
                    stripe_subscription_id=None,
                )
                logger.info(
                    "Downgraded user %s to free tier", user.user_id
                )

    async def get_subscription_status_async(
        self,
        user_id: str,
        user_repo: UserRepository,
    ) -> dict[str, Any]:
        """Get subscription status using a DB-backed user repository.

        Args:
            user_id: Public user identifier.
            user_repo: Database-backed ``UserRepository`` for this request.

        Returns:
            Dict with subscription details.

        Raises:
            ValueError: If user not found.
        """
        user = await user_repo.get_by_user_id(user_id)
        if user is None:
            raise ValueError(f"User not found: {user_id}")

        return {
            "user_id": user_id,
            "tier": user.tier,
            "stripe_subscription_id": user.stripe_subscription_id,
            "is_active": (
                user.tier != BillingTier.FREE.value
                or user.stripe_subscription_id is None
            ),
        }


# Singleton instance
billing_service = BillingService()
