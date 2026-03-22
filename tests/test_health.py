"""Health and readiness endpoint tests (#39).

Tests for GET /health and GET /ready using httpx AsyncClient.
"""

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from api.routers import health


@pytest.fixture
def app():
    """Create a minimal FastAPI app that mounts only the health router.

    The health router is tested in isolation here; wiring into the full
    application factory happens in a later task.
    """
    application = FastAPI(title="Parsify Health Test")
    application.include_router(health.router)
    return application


@pytest_asyncio.fixture
async def client(app):
    """Async HTTP client backed by the ASGI app."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


# ---------------------------------------------------------------------------
# Liveness — GET /health
# ---------------------------------------------------------------------------


class TestHealthEndpoint:
    """Tests for GET /health."""

    @pytest.mark.asyncio
    async def test_health_returns_200(self, client: AsyncClient) -> None:
        """GET /health always returns 200 with core fields present."""
        response = await client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "version" in data
        assert "uptime_seconds" in data

    @pytest.mark.asyncio
    async def test_health_includes_checks(self, client: AsyncClient) -> None:
        """GET /health includes a 'checks' dict with database and redis keys."""
        response = await client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert "checks" in data
        checks = data["checks"]
        assert "database" in checks
        assert "redis" in checks

    @pytest.mark.asyncio
    async def test_health_status_value(self, client: AsyncClient) -> None:
        """GET /health always reports status as 'healthy' regardless of deps."""
        response = await client.get("/health")

        assert response.json()["status"] == "healthy"

    @pytest.mark.asyncio
    async def test_health_uptime_is_non_negative(self, client: AsyncClient) -> None:
        """Uptime reported by /health is a non-negative number."""
        response = await client.get("/health")

        uptime = response.json()["uptime_seconds"]
        assert isinstance(uptime, (int, float))
        assert uptime >= 0

    @pytest.mark.asyncio
    async def test_health_check_values_are_strings(self, client: AsyncClient) -> None:
        """Each check value is either 'ok' or 'error'."""
        response = await client.get("/health")

        checks = response.json()["checks"]
        for key, value in checks.items():
            assert value in ("ok", "error"), (
                f"Unexpected check value for '{key}': {value!r}"
            )


# ---------------------------------------------------------------------------
# Readiness — GET /ready
# ---------------------------------------------------------------------------


class TestReadinessEndpoint:
    """Tests for GET /ready."""

    @pytest.mark.asyncio
    async def test_readiness_returns_status(self, client: AsyncClient) -> None:
        """GET /ready response contains the three required boolean fields."""
        response = await client.get("/ready")

        # Accept either 200 (all deps up) or 503 (some dep down) — both
        # are valid outcomes in a test environment where DB/Redis may not
        # be running.
        assert response.status_code in (200, 503)
        data = response.json()
        assert "ready" in data
        assert "database" in data
        assert "redis" in data

    @pytest.mark.asyncio
    async def test_readiness_fields_are_booleans(self, client: AsyncClient) -> None:
        """All fields in the /ready response are booleans."""
        response = await client.get("/ready")

        data = response.json()
        assert isinstance(data["ready"], bool)
        assert isinstance(data["database"], bool)
        assert isinstance(data["redis"], bool)

    @pytest.mark.asyncio
    async def test_readiness_ready_reflects_deps(self, client: AsyncClient) -> None:
        """'ready' is True only when both database and redis are True."""
        response = await client.get("/ready")

        data = response.json()
        expected_ready = data["database"] and data["redis"]
        assert data["ready"] == expected_ready

    @pytest.mark.asyncio
    async def test_readiness_status_code_matches_ready(
        self, client: AsyncClient
    ) -> None:
        """Status code is 200 when ready=True, 503 when ready=False."""
        response = await client.get("/ready")

        data = response.json()
        if data["ready"]:
            assert response.status_code == 200
        else:
            assert response.status_code == 503
