"""Per-key rate limiting middleware (#24).

Uses slowapi with in-memory backend for Phase 1-2.
Will switch to Redis backend in Phase 3 for distributed rate limiting.

See ADR-005 for design rationale.
"""

import logging

from fastapi import Request
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse

from ..config import settings

logger = logging.getLogger(__name__)


def _get_key_from_request(request: Request) -> str:
    """Extract rate limit key from request.

    Uses the API key prefix if authenticated, otherwise falls back
    to the client IP address.
    """
    auth_header = request.headers.get("authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        # Use first 16 chars as key identifier (includes prefix)
        return token[:16]
    return get_remote_address(request)


limiter = Limiter(
    key_func=_get_key_from_request,
    default_limits=[settings.rate_limit_free],
    storage_uri="memory://",
)


def rate_limit_exceeded_handler(
    request: Request, exc: RateLimitExceeded
) -> JSONResponse:
    """Custom 429 response with Retry-After header."""
    retry_after = getattr(exc, "retry_after", 60)
    return JSONResponse(
        status_code=429,
        content={
            "error": {
                "code": "RATE_LIMIT_EXCEEDED",
                "message": f"Rate limit exceeded. Try again in {retry_after} seconds.",
                "details": {"limit": str(exc.detail), "retry_after": retry_after},
            }
        },
        headers={"Retry-After": str(retry_after)},
    )
