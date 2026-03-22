"""FastAPI dependency for injecting an async database session.

Usage::

    from fastapi import Depends
    from sqlalchemy.ext.asyncio import AsyncSession

    from api.db.session import get_db_session

    @router.get("/items")
    async def list_items(db: AsyncSession = Depends(get_db_session)):
        ...
"""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from api.db.engine import async_session_factory

logger = logging.getLogger(__name__)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Yield a transactional ``AsyncSession`` for use as a FastAPI dependency.

    The session is committed automatically when the request handler returns
    without raising an exception.  On any exception the transaction is
    rolled back before the error is re-raised, ensuring database integrity.

    Yields:
        An ``AsyncSession`` bound to the module-level connection pool.

    Raises:
        Exception: Re-raises any exception from the request handler after
            rolling back the current transaction.
    """
    factory = async_session_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
