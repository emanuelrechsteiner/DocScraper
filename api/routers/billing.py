"""Billing router — Stripe checkout and webhooks (#27, #28)."""

import uuid

from fastapi import APIRouter, HTTPException, Request

from ..models.schemas import (
    APIResponse,
    CheckoutRequest,
    MetaResponse,
)
from ..services.billing import billing_service

router = APIRouter(prefix="/billing", tags=["billing"])


@router.get("/plans", response_model=APIResponse)
async def list_plans() -> APIResponse:
    """List all available billing plans (#26).

    Returns:
        APIResponse with plan details for each tier.
    """
    plans = billing_service.get_plans()
    return APIResponse(
        data=[
            {
                "tier": p["tier"].value,
                "name": p["name"],
                "description": p["description"],
                "requests_per_hour": p["requests_per_hour"],
                "max_pages_per_request": p["max_pages_per_request"],
                "max_concurrent_jobs": p["max_concurrent_jobs"],
                "price_monthly_cents": p["price_monthly_cents"],
            }
            for p in plans
        ],
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.post("/checkout", response_model=APIResponse)
async def create_checkout(
    request: CheckoutRequest, user_id: str = "user_default"
) -> APIResponse:
    """Create a Stripe checkout session for plan upgrade (#27).

    Args:
        request: Target tier and redirect URLs.
        user_id: Authenticated user ID.

    Returns:
        APIResponse with checkout URL and session ID.

    Raises:
        HTTPException: 400 if configuration or validation error.
    """
    try:
        result = await billing_service.create_checkout_session(
            user_id=user_id,
            tier=request.tier,
            success_url=str(request.success_url),
            cancel_url=str(request.cancel_url),
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail={"code": "CHECKOUT_ERROR", "message": str(exc)},
        ) from exc

    return APIResponse(
        data=result,
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.post("/webhooks")
async def stripe_webhook(request: Request) -> dict[str, str]:
    """Handle incoming Stripe webhook events (#28).

    Verifies the webhook signature and processes the event.

    Args:
        request: Raw HTTP request containing the Stripe event payload.

    Returns:
        Acknowledgement dict.

    Raises:
        HTTPException: 400 if signature verification fails.
    """
    payload = await request.body()
    signature = request.headers.get("stripe-signature", "")

    try:
        result = await billing_service.handle_webhook_event(payload, signature)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail={"code": "WEBHOOK_ERROR", "message": str(exc)},
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail={"code": "WEBHOOK_VERIFICATION_FAILED", "message": str(exc)},
        ) from exc

    return {"status": "ok", "event_type": result["event_type"]}


@router.get("/subscription", response_model=APIResponse)
async def get_subscription(user_id: str = "user_default") -> APIResponse:
    """Get current subscription status (#27).

    Args:
        user_id: Authenticated user ID.

    Returns:
        APIResponse with subscription details.

    Raises:
        HTTPException: 404 if user not found.
    """
    try:
        status = billing_service.get_subscription_status(user_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail={"code": "USER_NOT_FOUND", "message": str(exc)},
        ) from exc

    return APIResponse(
        data=status,
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
