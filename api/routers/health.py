"""Health and readiness endpoints (#39).

GET /health — Liveness check with dependency status and uptime.
GET /ready  — Readiness check; returns 503 if dependencies are down.
"""

import logging
import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

_STARTUP_TIME: float = time.monotonic()

router = APIRouter(tags=["health"])

VERSION = "0.3.0"


async def _check_database() -> bool:
    """Probe the database with a trivial query.

    Returns:
        True if the database is reachable, False on any failure.
    """
    try:
        from sqlalchemy import text
        from sqlalchemy.ext.asyncio import create_async_engine

        from api.config import settings

        engine = create_async_engine(settings.database_url, pool_pre_ping=True)
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        await engine.dispose()
        return True
    except Exception:
        logger.debug("Database health check failed", exc_info=True)
        return False


async def _check_redis() -> bool:
    """Probe Redis with a PING command.

    Returns:
        True if Redis is reachable, False on any failure.
    """
    try:
        import redis.asyncio as aioredis

        from api.config import settings

        client = aioredis.from_url(settings.redis_url, socket_connect_timeout=2)
        await client.ping()
        await client.aclose()
        return True
    except Exception:
        logger.debug("Redis health check failed", exc_info=True)
        return False


@router.get("/health")
async def health_check() -> JSONResponse:
    """Liveness probe — always returns 200 with dependency status and uptime.

    Returns:
        JSON payload with status, version, uptime_seconds, and per-dependency
        check results.
    """
    db_ok = await _check_database()
    redis_ok = await _check_redis()

    payload = {
        "status": "healthy",
        "version": VERSION,
        "uptime_seconds": round(time.monotonic() - _STARTUP_TIME, 2),
        "checks": {
            "database": "ok" if db_ok else "error",
            "redis": "ok" if redis_ok else "error",
        },
    }
    return JSONResponse(content=payload, status_code=200)


@router.get("/ready")
async def readiness_check() -> JSONResponse:
    """Readiness probe — returns 503 when any required dependency is unavailable.

    Returns:
        200 with ``ready: true`` when all dependencies are up.
        503 with ``ready: false`` when one or more dependencies are down.
    """
    db_ok = await _check_database()
    redis_ok = await _check_redis()
    all_ready = db_ok and redis_ok

    payload = {
        "ready": all_ready,
        "database": db_ok,
        "redis": redis_ok,
    }
    status_code = 200 if all_ready else 503
    return JSONResponse(content=payload, status_code=status_code)
