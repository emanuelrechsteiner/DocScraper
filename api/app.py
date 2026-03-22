"""Parsify REST API application factory."""

import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        A fully configured FastAPI application instance with all routers
        registered under the /api/v1 prefix.
    """
    app = FastAPI(
        title="Parsify API",
        description="Documentation scraping and processing REST API",
        version="0.1.0",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    from .routers import scrape

    app.include_router(scrape.router, prefix="/api/v1")

    logger.info("Parsify API application created (version 0.1.0)")
    return app


app = create_app()
