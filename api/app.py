"""Parsify REST API application factory."""

import logging

from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded

from .middleware.rate_limit import limiter, rate_limit_exceeded_handler
from .middleware.usage import UsageTrackingMiddleware

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Registers all routers under /api/v1 and attaches middleware
    for authentication, rate limiting, and usage tracking.

    Returns:
        A fully configured FastAPI application instance.
    """
    app = FastAPI(
        title="Parsify API",
        description="Documentation scraping and processing REST API",
        version="0.2.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
    )

    # --- Middleware (order matters: last added = first executed) ---

    # Usage tracking — records every request
    app.add_middleware(UsageTrackingMiddleware)

    # Rate limiting
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

    # --- Routers ---

    from .routers import auth, billing, jobs, process, scrape, usage

    app.include_router(scrape.router, prefix="/api/v1")
    app.include_router(jobs.router, prefix="/api/v1")
    app.include_router(process.router, prefix="/api/v1")
    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(billing.router, prefix="/api/v1")
    app.include_router(usage.router, prefix="/api/v1")

    # --- Health check ---

    @app.get("/health")
    async def health_check() -> dict[str, str]:
        return {"status": "healthy", "version": "0.2.0"}

    logger.info("Parsify API application created (version 0.2.0)")
    return app


app = create_app()
