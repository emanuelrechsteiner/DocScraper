"""Usage dashboard router — usage stats endpoints (#29)."""

import uuid

from fastapi import APIRouter, Query

from ..models.schemas import APIResponse, BillingTier, MetaResponse
from ..services.auth_service import auth_service
from ..services.usage import usage_service

router = APIRouter(prefix="/usage", tags=["usage"])


@router.get("", response_model=APIResponse)
async def get_usage_summary(
    user_id: str = "user_default",
    key_id: str | None = Query(default=None, description="Specific key ID"),
) -> APIResponse:
    """Get usage summary for the current billing period (#29).

    Args:
        user_id: Authenticated user ID.
        key_id: Optional specific key to check.

    Returns:
        APIResponse with usage summary and overage status.
    """
    user = auth_service.get_user(user_id)
    tier = user.tier if user else BillingTier.FREE

    effective_key_id = key_id or user_id
    summary = usage_service.get_summary(effective_key_id, tier)
    overage = usage_service.check_overage(effective_key_id, tier)

    return APIResponse(
        data={**summary, "overage": overage},
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.get("/daily", response_model=APIResponse)
async def get_daily_usage(
    user_id: str = "user_default",
    key_id: str | None = Query(default=None),
    days: int = Query(default=30, ge=1, le=90, description="Number of days"),
) -> APIResponse:
    """Get daily usage breakdown (#29).

    Args:
        user_id: Authenticated user ID.
        key_id: Optional specific key to check.
        days: Number of days to return.

    Returns:
        APIResponse with daily usage entries.
    """
    effective_key_id = key_id or user_id
    breakdown = usage_service.get_daily_breakdown(effective_key_id, days)

    return APIResponse(
        data=breakdown,
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
