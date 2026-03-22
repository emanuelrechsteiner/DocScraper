"""API key authentication middleware (#20).

Provides FastAPI dependencies for extracting and verifying API keys
from the Authorization header. Keys use Bearer scheme: `Authorization: Bearer pk_xxx...`

See ADR-004 for design rationale.
"""

import logging
from typing import Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..services.auth_service import APIKeyData, auth_service

logger = logging.getLogger(__name__)

# HTTPBearer extracts the token from `Authorization: Bearer <token>`
_bearer_scheme = HTTPBearer(auto_error=False)


async def get_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(_bearer_scheme),
) -> Optional[APIKeyData]:
    """Extract and verify API key from the Authorization header.

    This dependency does NOT raise on missing keys — use `require_auth`
    for endpoints that require authentication.

    Returns:
        APIKeyData if a valid key is provided, None otherwise.
    """
    if credentials is None:
        return None

    key_data = auth_service.verify_api_key(credentials.credentials)
    if key_data is None:
        return None

    return key_data


async def require_auth(
    key_data: Optional[APIKeyData] = Depends(get_api_key),
) -> APIKeyData:
    """Require a valid API key — raises 401 if missing or invalid.

    Use this as a dependency on protected endpoints:

        @router.post("/scrape")
        async def scrape(key: APIKeyData = Depends(require_auth)):
            ...

    Returns:
        Verified APIKeyData.

    Raises:
        HTTPException: 401 if no valid key provided.
    """
    if key_data is None:
        raise HTTPException(
            status_code=401,
            detail={
                "code": "UNAUTHORIZED",
                "message": "Missing or invalid API key. Include: Authorization: Bearer pk_...",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    return key_data


def get_user_id_from_key(key_data: APIKeyData) -> str:
    """Extract the user_id from a verified API key."""
    return key_data.user_id
