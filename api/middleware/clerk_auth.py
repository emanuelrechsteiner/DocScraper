"""Clerk JWT authentication for the developer dashboard.

Verifies RS256 JWTs issued by Clerk and resolves the Clerk user ID
to a Parsify User record, auto-creating on first login.
"""

import logging
import time
from typing import Optional

import httpx
import jwt as pyjwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import settings
from ..db.models import User
from ..db.repositories import UserRepository
from ..db.session import get_db_session

logger = logging.getLogger(__name__)

_bearer_scheme = HTTPBearer(auto_error=False)

# JWKS cache
_jwks_cache: dict = {}
_jwks_cache_ttl: float = 0
_JWKS_CACHE_DURATION = 3600  # 1 hour


async def _get_jwks() -> dict:
    """Fetch and cache Clerk's JWKS (JSON Web Key Set)."""
    global _jwks_cache, _jwks_cache_ttl

    now = time.time()
    if _jwks_cache and now < _jwks_cache_ttl:
        return _jwks_cache

    if not settings.clerk_jwks_url:
        raise HTTPException(
            status_code=500,
            detail="Clerk JWKS URL not configured",
        )

    async with httpx.AsyncClient() as client:
        resp = await client.get(settings.clerk_jwks_url, timeout=10)
        resp.raise_for_status()
        _jwks_cache = resp.json()
        _jwks_cache_ttl = now + _JWKS_CACHE_DURATION

    return _jwks_cache


def _decode_jwt(token: str, jwks: dict) -> dict:
    """Decode and verify a Clerk JWT using RS256.

    Args:
        token: The raw JWT string.
        jwks: The JWKS dict from Clerk.

    Returns:
        Decoded token payload.

    Raises:
        HTTPException: If token is invalid or expired.
    """
    try:
        # Get the signing key from JWKS
        unverified_header = pyjwt.get_unverified_header(token)
        kid = unverified_header.get("kid")

        rsa_key = None
        for key in jwks.get("keys", []):
            if key.get("kid") == kid:
                rsa_key = pyjwt.algorithms.RSAAlgorithm.from_jwk(key)
                break

        if rsa_key is None:
            raise HTTPException(
                status_code=401,
                detail="Unable to find signing key",
            )

        payload = pyjwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            options={"verify_aud": False},
        )
        return payload

    except pyjwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except pyjwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail=f"Invalid token: {exc}")


async def get_dashboard_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(_bearer_scheme),
    db: AsyncSession = Depends(get_db_session),
) -> User:
    """Verify Clerk JWT and resolve to a Parsify User.

    Auto-creates the User record on first dashboard login.

    Args:
        credentials: Bearer token from Authorization header.
        db: Async database session.

    Returns:
        The authenticated User ORM object.

    Raises:
        HTTPException: 401 if token is missing/invalid.
    """
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    jwks = await _get_jwks()
    payload = _decode_jwt(credentials.credentials, jwks)

    clerk_user_id = payload.get("sub")
    if not clerk_user_id:
        raise HTTPException(status_code=401, detail="Token missing subject claim")

    repo = UserRepository(db)
    user = await repo.get_by_clerk_user_id(clerk_user_id)

    if user is None:
        # Auto-create user on first dashboard login
        email = payload.get(
            "email",
            payload.get("email_addresses", [{}])[0].get(
                "email_address", f"{clerk_user_id}@clerk.user"
            ),
        )
        name = payload.get("name", payload.get("first_name", ""))
        user = await repo.create(email=email, name=name or None)
        user.clerk_user_id = clerk_user_id
        await db.flush()
        logger.info(
            "Auto-created user %s for Clerk ID %s", user.user_id, clerk_user_id
        )

    return user
