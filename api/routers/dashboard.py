"""Dashboard API endpoints for the Parsify developer console.

All endpoints require Clerk JWT authentication via the
``get_dashboard_user`` dependency.
"""

import logging

from fastapi import APIRouter, Depends

from ..db.models import User
from ..middleware.clerk_auth import get_dashboard_user

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/me")
async def get_current_user(user: User = Depends(get_dashboard_user)):
    """Return the authenticated dashboard user's profile.

    Returns:
        JSON object with user details.
    """
    return {
        "data": {
            "user_id": user.user_id,
            "email": user.email,
            "name": user.name,
            "tier": user.tier,
            "clerk_user_id": user.clerk_user_id,
            "stripe_customer_id": user.stripe_customer_id,
            "created_at": user.created_at.isoformat() if user.created_at else None,
        }
    }
