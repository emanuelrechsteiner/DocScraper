"""Request ID middleware (#40).

Assigns a unique trace identifier to every inbound request so that all
log lines emitted during the request lifecycle can be correlated.

The ID is taken from the ``X-Request-ID`` request header when the
client supplies one; otherwise a short random identifier is generated
with the ``req_`` prefix.  The resolved ID is stored on
``request.state.request_id`` for downstream use (e.g. routers that
attach it to log records) and echoed back in the response via the same
``X-Request-ID`` header.

Usage (in ``app.py``)::

    from api.middleware.request_id import RequestIDMiddleware
    app.add_middleware(RequestIDMiddleware)
"""

import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

#: The HTTP header used to propagate the request trace identifier.
REQUEST_ID_HEADER = "X-Request-ID"


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Starlette middleware that ensures every request carries a trace ID.

    Behaviour:

    * If the client sends ``X-Request-ID`` the value is reused as-is.
    * Otherwise a new ID is generated: ``req_<first 12 hex chars of uuid4>``.
    * The resolved ID is attached to ``request.state.request_id``.
    * The ID is added to the response under the ``X-Request-ID`` header.
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Attach a request ID to the request state and response headers.

        Args:
            request: The incoming Starlette request.
            call_next: Callable that invokes the next middleware or route handler.

        Returns:
            The response with the ``X-Request-ID`` header set.
        """
        # Honour client-supplied IDs; generate one otherwise.
        request_id = request.headers.get(REQUEST_ID_HEADER)
        if not request_id:
            request_id = f"req_{uuid.uuid4().hex[:12]}"

        # Make the ID available to route handlers and other middleware.
        request.state.request_id = request_id

        response = await call_next(request)

        # Echo the ID back so clients can correlate responses to requests.
        response.headers[REQUEST_ID_HEADER] = request_id

        return response
