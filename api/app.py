"""Parsify REST API application factory."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded

from .config import settings
from .middleware.logging_config import setup_logging
from .middleware.rate_limit import limiter, rate_limit_exceeded_handler
from .middleware.request_id import RequestIDMiddleware
from .middleware.usage import UsageTrackingMiddleware

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage application lifecycle: initialise and dispose the DB engine.

    Args:
        app: The FastAPI application instance.

    Yields:
        Control to the application while it is running.
    """
    from .db.engine import create_async_engine_from_settings, dispose_engine

    create_async_engine_from_settings()
    logger.info("Database engine initialized")
    yield
    await dispose_engine()
    logger.info("Database engine disposed")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Registers all routers under /api/v1 and attaches middleware
    for authentication, rate limiting, usage tracking, and request IDs.

    Returns:
        A fully configured FastAPI application instance.
    """
    from .middleware.sentry_config import init_sentry

    init_sentry()
    setup_logging()

    app = FastAPI(
        title="Parsify API",
        description="Documentation scraping and processing REST API",
        version="0.3.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )

    # --- Middleware (order matters: last added = first executed) ---

    # CORS for dashboard frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.dashboard_origin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request ID propagation — must be outermost to stamp every response
    app.add_middleware(RequestIDMiddleware)

    # Usage tracking — records every request
    app.add_middleware(UsageTrackingMiddleware)

    # Rate limiting
    app.state.limiter = limiter
    # slowapi's handler signature is narrower than Starlette's typed contract.
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)  # type: ignore[arg-type]

    # --- Routers ---

    from .routers import auth, billing, dashboard, health, jobs, process, scrape, usage

    app.include_router(health.router)
    app.include_router(scrape.router, prefix="/api/v1")
    app.include_router(jobs.router, prefix="/api/v1")
    app.include_router(process.router, prefix="/api/v1")
    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(billing.router, prefix="/api/v1")
    app.include_router(usage.router, prefix="/api/v1")
    app.include_router(dashboard.router, prefix="/api/v1")

    logger.info("Parsify API application created (version 0.3.0)")
    return app


app = create_app()
