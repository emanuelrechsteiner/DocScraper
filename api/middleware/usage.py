"""Usage tracking middleware (#25).

Records API usage per request for billing and analytics.
Runs as Starlette middleware — captures every request/response cycle.

Note: This middleware intentionally uses the in-memory ``usage_service``
for performance. Writing every request to PostgreSQL synchronously would
add unacceptable latency to every API call. The ``UsageRepository`` is
used in route handlers where per-key DB writes are explicitly required.
A future improvement could batch-flush these records to the DB
asynchronously (e.g. via ARQ background task).
"""

import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from ..services.usage import usage_service

logger = logging.getLogger(__name__)


class UsageTrackingMiddleware(BaseHTTPMiddleware):
    """Records API usage metrics for every request.

    Captures: endpoint, method, status code, response time, and
    the API key used (if any).
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Record usage after each request completes."""
        start = time.monotonic()
        response = await call_next(request)
        elapsed_ms = (time.monotonic() - start) * 1000

        # Extract key ID from auth header (if present)
        key_id = None
        auth_header = request.headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            key_id = auth_header[7:][:16]

        # Skip health checks and docs from usage tracking
        path = request.url.path
        if path in ("/health", "/api/docs", "/api/openapi.json", "/api/redoc"):
            return response

        usage_service.record(
            endpoint=path,
            method=request.method,
            status_code=response.status_code,
            response_time_ms=round(elapsed_ms, 2),
            key_id=key_id,
        )

        return response
