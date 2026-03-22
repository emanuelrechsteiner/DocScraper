"""Async SQLAlchemy engine and session factory for the Parsify API.

Provides a module-level singleton engine and session maker, plus a
``dispose_engine()`` coroutine for clean shutdown.
"""

from __future__ import annotations

import logging
from urllib.parse import urlparse

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from api.config import settings

logger = logging.getLogger(__name__)

_engine: AsyncEngine | None = None
_session_maker: async_sessionmaker[AsyncSession] | None = None


def create_async_engine_from_settings() -> AsyncEngine:
    """Create (or return the existing) async SQLAlchemy engine.

    Uses ``settings.database_url`` with a connection pool of size 10,
    max overflow 20, and pre-ping enabled to detect stale connections.
    Only the host portion of the URL is logged — credentials are never
    written to the log.

    Returns:
        The module-level ``AsyncEngine`` singleton.
    """
    global _engine
    if _engine is not None:
        return _engine

    url = settings.database_url
    parsed = urlparse(url)
    logger.info(
        "Creating async database engine",
        extra={"host": parsed.hostname, "database": parsed.path.lstrip("/")},
    )

    _engine = create_async_engine(
        url,
        echo=settings.database_echo,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
    )
    return _engine


def async_session_factory() -> async_sessionmaker[AsyncSession]:
    """Create (or return the existing) async session maker.

    The session maker is bound to the engine returned by
    :func:`create_async_engine_from_settings`.  Sessions are configured
    with ``expire_on_commit=False`` so that ORM objects remain accessible
    after a commit without issuing additional SELECT queries.

    Returns:
        The module-level ``async_sessionmaker[AsyncSession]`` singleton.
    """
    global _session_maker
    if _session_maker is not None:
        return _session_maker

    engine = create_async_engine_from_settings()
    _session_maker = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    return _session_maker


async def dispose_engine() -> None:
    """Dispose the connection pool and reset both module-level singletons.

    Should be called during application shutdown (e.g. in a FastAPI
    ``lifespan`` shutdown handler) to cleanly close all pooled connections.
    """
    global _engine, _session_maker
    if _engine is not None:
        await _engine.dispose()
        logger.info("Database engine disposed")
    _engine = None
    _session_maker = None
