"""Tests for structured logging and request ID middleware (#40).

Covers:
* JSONFormatter — correct JSON shape, optional extra fields, exception info.
* RequestIDMiddleware — header propagation and client-supplied ID preservation.
"""

from __future__ import annotations

import json
import logging

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from api.middleware.logging_config import JSONFormatter
from api.middleware.request_id import REQUEST_ID_HEADER, RequestIDMiddleware
from api.app import create_app


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_record(
    message: str = "test message",
    level: int = logging.INFO,
    name: str = "api.test",
    **extras: object,
) -> logging.LogRecord:
    """Create a minimal LogRecord, optionally with extra attributes."""
    record = logging.LogRecord(
        name=name,
        level=level,
        pathname="",
        lineno=0,
        msg=message,
        args=(),
        exc_info=None,
    )
    for key, value in extras.items():
        setattr(record, key, value)
    return record


# ---------------------------------------------------------------------------
# TestJSONFormatter
# ---------------------------------------------------------------------------


class TestJSONFormatter:
    """Unit tests for JSONFormatter."""

    def test_format_produces_valid_json(self) -> None:
        """Formatted output must be parseable as JSON."""
        formatter = JSONFormatter()
        record = _make_record("hello world")

        output = formatter.format(record)
        parsed = json.loads(output)

        assert parsed["message"] == "hello world"
        assert parsed["level"] == "INFO"
        assert parsed["logger"] == "api.test"
        # Timestamp must be present and non-empty.
        assert "timestamp" in parsed
        assert parsed["timestamp"]

    def test_format_level_name_matches_record(self) -> None:
        """Level name in JSON matches the LogRecord level."""
        formatter = JSONFormatter()

        for level, expected in (
            (logging.DEBUG, "DEBUG"),
            (logging.WARNING, "WARNING"),
            (logging.ERROR, "ERROR"),
        ):
            record = _make_record(level=level)
            parsed = json.loads(formatter.format(record))
            assert parsed["level"] == expected

    def test_format_includes_extra_fields(self) -> None:
        """Optional request-tracing extras are included when present."""
        formatter = JSONFormatter()
        record = _make_record(
            "request handled",
            request_id="req_abc123",
            method="POST",
            path="/api/v1/scrape",
            status_code=202,
            duration_ms=45.7,
        )

        parsed = json.loads(formatter.format(record))

        assert parsed["request_id"] == "req_abc123"
        assert parsed["method"] == "POST"
        assert parsed["path"] == "/api/v1/scrape"
        assert parsed["status_code"] == 202
        assert parsed["duration_ms"] == 45.7

    def test_format_omits_missing_extra_fields(self) -> None:
        """Optional fields are absent from JSON when not set on the record."""
        formatter = JSONFormatter()
        record = _make_record("bare record")

        parsed = json.loads(formatter.format(record))

        for field in ("request_id", "method", "path", "status_code", "duration_ms"):
            assert field not in parsed, f"Unexpected field '{field}' in output"

    def test_format_includes_exception_info(self) -> None:
        """Exception info is serialised into an 'exception' key."""
        formatter = JSONFormatter()
        try:
            raise ValueError("something went wrong")
        except ValueError:
            import sys

            exc_info = sys.exc_info()

        record = logging.LogRecord(
            name="api.test",
            level=logging.ERROR,
            pathname="",
            lineno=0,
            msg="caught an error",
            args=(),
            exc_info=exc_info,
        )

        parsed = json.loads(formatter.format(record))

        assert "exception" in parsed
        exc = parsed["exception"]
        assert exc["type"] == "ValueError"
        assert "something went wrong" in exc["value"]
        assert isinstance(exc["traceback"], list)

    def test_format_output_is_single_line(self) -> None:
        """Each log record must produce exactly one line (no embedded newlines)."""
        formatter = JSONFormatter()
        record = _make_record("single line output")
        output = formatter.format(record)
        assert "\n" not in output


# ---------------------------------------------------------------------------
# Fixtures for middleware tests
# ---------------------------------------------------------------------------


@pytest.fixture()
def app_with_request_id():
    """FastAPI app with RequestIDMiddleware registered."""
    application = create_app()
    application.add_middleware(RequestIDMiddleware)
    return application


@pytest_asyncio.fixture()
async def client(app_with_request_id):
    """Async HTTP client backed by the test app."""
    transport = ASGITransport(app=app_with_request_id)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ---------------------------------------------------------------------------
# TestRequestIDMiddleware
# ---------------------------------------------------------------------------


class TestRequestIDMiddleware:
    """Integration tests for RequestIDMiddleware."""

    @pytest.mark.asyncio
    async def test_response_has_request_id_header(self, client: AsyncClient) -> None:
        """Every response carries an X-Request-ID header."""
        response = await client.get("/health")

        assert response.status_code == 200
        assert REQUEST_ID_HEADER in response.headers
        request_id = response.headers[REQUEST_ID_HEADER]
        assert request_id.startswith("req_")
        # Generated IDs have prefix + 12 hex chars = 16 chars total.
        assert len(request_id) == len("req_") + 12

    @pytest.mark.asyncio
    async def test_client_request_id_preserved(self, client: AsyncClient) -> None:
        """A client-supplied X-Request-ID is echoed back unchanged."""
        custom_id = "my-trace-id-9999"
        response = await client.get(
            "/health", headers={REQUEST_ID_HEADER: custom_id}
        )

        assert response.status_code == 200
        assert response.headers[REQUEST_ID_HEADER] == custom_id

    @pytest.mark.asyncio
    async def test_generated_ids_are_unique(self, client: AsyncClient) -> None:
        """Two requests without a client ID receive different generated IDs."""
        r1 = await client.get("/health")
        r2 = await client.get("/health")

        id1 = r1.headers[REQUEST_ID_HEADER]
        id2 = r2.headers[REQUEST_ID_HEADER]
        assert id1 != id2

    @pytest.mark.asyncio
    async def test_empty_client_id_generates_new_id(
        self, client: AsyncClient
    ) -> None:
        """An empty X-Request-ID header is treated as absent."""
        response = await client.get("/health", headers={REQUEST_ID_HEADER: ""})

        # An empty string is falsy — middleware should generate a new ID.
        returned_id = response.headers[REQUEST_ID_HEADER]
        assert returned_id.startswith("req_")
