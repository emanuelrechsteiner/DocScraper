"""API key authentication middleware (#20).

Provides FastAPI dependencies for extracting and verifying API keys
from the Authorization header. Keys use Bearer scheme: ``Authorization: Bearer pk_xxx...``

See ADR-004 for design rationale.
"""

import logging
from typing import Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.models import APIKey
from ..db.repositories import APIKeyRepository
from ..db.session import get_db_session

logger = logging.getLogger(__name__)

# HTTPBearer extracts the token from `Authorization: Bearer <token>`
_bearer_scheme = HTTPBearer(auto_error=False)


async def get_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(_bearer_scheme),
    db: AsyncSession = Depends(get_db_session),
) -> Optional[APIKey]:
    """Extract and verify API key from the Authorization header.

    This dependency does NOT raise on missing keys — use ``require_auth``
    for endpoints that require authentication.

    Args:
        credentials: Parsed Bearer credentials (may be ``None``).
        db: Injected async database session.

    Returns:
        ``APIKey`` ORM object if a valid active key is provided, ``None`` otherwise.
    """
    if credentials is None:
        return None

    repo = APIKeyRepository(db)
    api_key = await repo.verify(credentials.credentials)
    return api_key


async def require_auth(
    api_key: Optional[APIKey] = Depends(get_api_key),
) -> APIKey:
    """Require a valid API key — raises 401 if missing or invalid.

    Use this as a dependency on protected endpoints::

        @router.post("/scrape")
        async def scrape(key: APIKey = Depends(require_auth)):
            ...

    Args:
        api_key: Result of the ``get_api_key`` dependency.

    Returns:
        Verified ``APIKey`` ORM object.

    Raises:
        HTTPException: 401 if no valid key provided.
    """
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail={
                "code": "UNAUTHORIZED",
                "message": (
                    "Missing or invalid API key. Include: Authorization: Bearer pk_..."
                ),
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    return api_key


def get_user_id_from_key(api_key: APIKey) -> str:
    """Extract the user_id from a verified API key ORM object.

    Args:
        api_key: Verified ``APIKey`` ORM object.

    Returns:
        The owner's ``user_id`` string.
    """
    return api_key.user_id
