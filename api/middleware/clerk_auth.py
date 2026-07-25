"""Clerk JWT authentication for the developer dashboard.

Verifies RS256 JWTs issued by Clerk and resolves the Clerk user ID
to a Parsify User record, auto-creating on first login.

Security properties:
- Signature verified against Clerk's JWKS (RS256 only; algorithm and key-use
  are asserted to prevent key-confusion / ``alg`` downgrade attacks).
- Issuer (``iss``) verified when ``clerk_issuer`` is configured.
- Authorized party (``azp``) checked against an allowlist when configured,
  binding tokens to the expected frontend origin (Clerk session tokens carry
  ``azp`` rather than ``aud``).
- Account identity is the verified ``sub`` claim — never a client-supplied
  email — preventing account-squatting. Emails are trusted only when the token
  asserts ``email_verified``.
"""

import logging
import time

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


def _authorized_parties() -> list[str]:
    """Return the allowlist of acceptable ``azp`` values (may be empty)."""
    raw = settings.clerk_authorized_parties or settings.dashboard_origin
    return [p.strip() for p in raw.split(",") if p.strip()]


async def _get_jwks(force_refresh: bool = False) -> dict:
    """Fetch and cache Clerk's JWKS (JSON Web Key Set).

    Args:
        force_refresh: Bypass the TTL cache (used after a ``kid`` miss so that
            key rotation does not require a cache-duration outage).
    """
    global _jwks_cache, _jwks_cache_ttl

    now = time.time()
    if not force_refresh and _jwks_cache and now < _jwks_cache_ttl:
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


def _find_signing_key(jwks: dict, kid: str | None):
    """Locate the RS256 signing key for ``kid`` in the JWKS.

    Asserts the key's algorithm and intended use before trusting it, so a
    spoofed JWKS entry with a different ``alg``/``use`` cannot be used.

    Returns:
        The RSA public key, or ``None`` if no suitable key matches.
    """
    if not kid:
        return None
    for key in jwks.get("keys", []):
        if key.get("kid") != kid:
            continue
        if key.get("alg", "RS256") != "RS256":
            continue
        if key.get("use") not in (None, "sig"):
            continue
        return pyjwt.algorithms.RSAAlgorithm.from_jwk(key)
    return None


def _decode(token: str, rsa_key) -> dict:
    """Decode and verify a Clerk JWT with full claim validation."""
    decode_kwargs: dict = {
        "algorithms": ["RS256"],
        "options": {
            "require": ["exp", "iat", "sub"],
            "verify_exp": True,
            "verify_signature": True,
        },
    }
    # Clerk session tokens use `azp`, not `aud`; don't require `aud`.
    decode_kwargs["options"]["verify_aud"] = False
    # Issuer enforcement is mandatory whenever Clerk is configured (fail-closed).
    decode_kwargs["issuer"] = settings.clerk_issuer
    decode_kwargs["options"]["require"].append("iss")

    payload = pyjwt.decode(token, rsa_key, **decode_kwargs)

    # Bind the token to an expected frontend origin via `azp`. A missing `azp`
    # is rejected (not allowed to pass) whenever an allowlist is configured.
    allowed = _authorized_parties()
    if allowed and payload.get("azp") not in allowed:
        raise HTTPException(status_code=401, detail="Token party not allowed")

    return payload


async def _verify_token(token: str) -> dict:
    """Verify a Clerk JWT, refreshing the JWKS once on a ``kid`` miss."""
    # Fail closed on misconfiguration: issuer enforcement is mandatory.
    if not settings.clerk_issuer:
        logger.error("Clerk auth invoked but clerk_issuer is not configured")
        raise HTTPException(
            status_code=500, detail="Clerk issuer not configured"
        )

    try:
        unverified_header = pyjwt.get_unverified_header(token)
    except pyjwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail=f"Malformed token: {exc}")

    kid = unverified_header.get("kid")

    jwks = await _get_jwks()
    rsa_key = _find_signing_key(jwks, kid)
    if rsa_key is None:
        # Key may have rotated — force a single refresh before failing.
        jwks = await _get_jwks(force_refresh=True)
        rsa_key = _find_signing_key(jwks, kid)
    if rsa_key is None:
        raise HTTPException(status_code=401, detail="Unable to find signing key")

    try:
        return _decode(token, rsa_key)
    except pyjwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except pyjwt.InvalidIssuerError:
        raise HTTPException(status_code=401, detail="Invalid token issuer")
    except pyjwt.InvalidTokenError as exc:
        raise HTTPException(status_code=401, detail=f"Invalid token: {exc}")


def _resolve_email(payload: dict, clerk_user_id: str) -> tuple[str, bool]:
    """Return ``(email, is_verified)`` from the token.

    Only a claim explicitly marked ``email_verified`` is trusted as a real
    email. Otherwise a safe, identity-derived placeholder is used so a forged
    email claim can never squat a real address.
    """
    email_claim = payload.get("email")
    email_verified = bool(payload.get("email_verified"))
    if email_claim and email_verified:
        return email_claim, True
    return f"{clerk_user_id}@clerk.local", False


async def get_dashboard_user(
    credentials: HTTPAuthorizationCredentials | None = Security(_bearer_scheme),
    db: AsyncSession = Depends(get_db_session),
) -> User:
    """Verify a Clerk JWT and resolve it to a Parsify ``User``.

    Auto-creates (or links) the ``User`` record on first dashboard login,
    keyed on the verified Clerk subject.

    Raises:
        HTTPException: 401 if the token is missing/invalid; 409 if a verified
            email already belongs to a different account.
    """
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing authorization token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = await _verify_token(credentials.credentials)

    clerk_user_id = payload.get("sub")
    if not clerk_user_id:
        raise HTTPException(status_code=401, detail="Token missing subject claim")

    email, email_verified = _resolve_email(payload, clerk_user_id)
    name = payload.get("name") or payload.get("first_name") or None

    repo = UserRepository(db)
    try:
        return await repo.get_or_create_by_clerk_id(
            clerk_user_id=clerk_user_id,
            email=email,
            name=name,
            email_is_verified=email_verified,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
