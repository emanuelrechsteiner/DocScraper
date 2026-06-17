"""Security tests for Clerk dashboard authentication.

Covers the hardening of api/middleware/clerk_auth.py and the race-safe,
squat-proof user resolution in UserRepository.get_or_create_by_clerk_id.
"""

import pytest

from api.config import settings
from api.db.repositories import UserRepository
from api.middleware import clerk_auth


# ---------------------------------------------------------------------------
# Repository: identity is the Clerk sub, never a client-supplied email
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_creates_user_keyed_on_clerk_id(db_session):
    repo = UserRepository(db_session)
    user = await repo.get_or_create_by_clerk_id(
        clerk_user_id="user_clerk_A",
        email="a@example.com",
        email_is_verified=True,
    )
    assert user.clerk_user_id == "user_clerk_A"
    assert user.email == "a@example.com"
    assert user.tier == "free"


@pytest.mark.asyncio
async def test_second_call_returns_same_user(db_session):
    repo = UserRepository(db_session)
    first = await repo.get_or_create_by_clerk_id(
        "user_clerk_B", "b@example.com", email_is_verified=True
    )
    second = await repo.get_or_create_by_clerk_id(
        "user_clerk_B", "different@example.com", email_is_verified=True
    )
    # Same Clerk identity → same account, email is not used as the key.
    assert second.user_id == first.user_id
    assert second.email == "b@example.com"


@pytest.mark.asyncio
async def test_unverified_email_uses_safe_placeholder(db_session):
    """An unverified email must never become the stored address."""
    repo = UserRepository(db_session)
    user = await repo.get_or_create_by_clerk_id(
        "user_clerk_C",
        "victim@corp.com",  # would be a real address, but not verified
        email_is_verified=False,
    )
    # Not linked to the victim address; a placeholder derived from the sub.
    assert user.email != "victim@corp.com"


@pytest.mark.asyncio
async def test_links_to_existing_account_only_when_verified(db_session):
    repo = UserRepository(db_session)
    existing = await repo.create(email="owner@example.com")
    linked = await repo.get_or_create_by_clerk_id(
        "user_clerk_D", "owner@example.com", email_is_verified=True
    )
    assert linked.user_id == existing.user_id
    assert linked.clerk_user_id == "user_clerk_D"


@pytest.mark.asyncio
async def test_conflict_when_email_belongs_to_other_identity(db_session):
    repo = UserRepository(db_session)
    await repo.get_or_create_by_clerk_id(
        "user_clerk_E", "shared@example.com", email_is_verified=True
    )
    with pytest.raises(ValueError):
        await repo.get_or_create_by_clerk_id(
            "user_clerk_F", "shared@example.com", email_is_verified=True
        )


# ---------------------------------------------------------------------------
# Token helpers
# ---------------------------------------------------------------------------


def test_resolve_email_trusts_only_verified():
    email, verified = clerk_auth._resolve_email(
        {"email": "real@example.com", "email_verified": True}, "user_x"
    )
    assert (email, verified) == ("real@example.com", True)


def test_resolve_email_rejects_unverified():
    email, verified = clerk_auth._resolve_email(
        {"email": "forged@example.com", "email_verified": False}, "user_x"
    )
    assert verified is False
    assert email == "user_x@clerk.local"
    assert "forged@example.com" not in email


def test_resolve_email_handles_missing_email():
    email, verified = clerk_auth._resolve_email({}, "user_y")
    assert (email, verified) == ("user_y@clerk.local", False)


def test_find_signing_key_rejects_non_rs256():
    jwks = {"keys": [{"kid": "k1", "alg": "HS256", "use": "sig"}]}
    assert clerk_auth._find_signing_key(jwks, "k1") is None


def test_find_signing_key_rejects_encryption_use():
    jwks = {"keys": [{"kid": "k1", "alg": "RS256", "use": "enc"}]}
    assert clerk_auth._find_signing_key(jwks, "k1") is None


def test_find_signing_key_returns_none_for_missing_kid():
    jwks = {"keys": [{"kid": "k1", "alg": "RS256", "use": "sig"}]}
    assert clerk_auth._find_signing_key(jwks, "other") is None
    assert clerk_auth._find_signing_key(jwks, None) is None


def test_authorized_parties_defaults_to_dashboard_origin(monkeypatch):
    monkeypatch.setattr(settings, "clerk_authorized_parties", "")
    monkeypatch.setattr(settings, "dashboard_origin", "https://app.parsify.dev")
    assert clerk_auth._authorized_parties() == ["https://app.parsify.dev"]


def test_authorized_parties_parses_csv(monkeypatch):
    monkeypatch.setattr(
        settings, "clerk_authorized_parties", "https://a.dev, https://b.dev"
    )
    assert clerk_auth._authorized_parties() == ["https://a.dev", "https://b.dev"]
