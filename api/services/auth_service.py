"""API key authentication service.

Implements API key creation, verification, and management.
Keys use SHA-256 hashing with a visible prefix for identification.
See ADR-004 for design rationale.

Will be backed by PostgreSQL in Phase 3.
"""

import hashlib
import logging
import secrets
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime

from ..config import settings
from ..models.schemas import BillingTier

logger = logging.getLogger(__name__)


@dataclass
class UserData:
    """Internal representation of a user."""

    user_id: str
    email: str
    name: str | None = None
    tier: BillingTier = BillingTier.FREE
    stripe_customer_id: str | None = None
    stripe_subscription_id: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class APIKeyData:
    """Internal representation of an API key."""

    key_id: str
    user_id: str
    name: str
    prefix: str
    key_hash: str
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class AuthService:
    """Manages users and API keys.

    In-memory storage for Phase 1-2. Will be replaced by
    PostgreSQL-backed service in Phase 3.
    """

    def __init__(self) -> None:
        self._users: dict[str, UserData] = {}
        self._users_by_email: dict[str, str] = {}
        self._api_keys: dict[str, APIKeyData] = {}  # key_id -> key data
        self._key_hash_index: dict[str, str] = {}  # hash -> key_id

    @staticmethod
    def _hash_key(raw_key: str) -> str:
        """Produce a SHA-256 hex digest of the raw API key."""
        return hashlib.sha256(raw_key.encode()).hexdigest()

    def create_user(
        self, email: str, name: str | None = None
    ) -> UserData:
        """Register a new user.

        Args:
            email: User email address.
            name: Optional display name.

        Returns:
            The created UserData.

        Raises:
            ValueError: If email is already registered.
        """
        if email in self._users_by_email:
            raise ValueError(f"Email already registered: {email}")

        user_id = f"user_{uuid.uuid4().hex[:12]}"
        user = UserData(user_id=user_id, email=email, name=name)
        self._users[user_id] = user
        self._users_by_email[email] = user_id
        logger.info("Created user %s (%s)", user_id, email)
        return user

    def get_user(self, user_id: str) -> UserData | None:
        """Get user by ID."""
        return self._users.get(user_id)

    def get_user_by_email(self, email: str) -> UserData | None:
        """Get user by email."""
        uid = self._users_by_email.get(email)
        return self._users.get(uid) if uid else None

    def update_user(self, user_id: str, **kwargs: object) -> UserData | None:
        """Update user fields."""
        user = self._users.get(user_id)
        if user is None:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return user

    def create_api_key(self, user_id: str, name: str) -> tuple[APIKeyData, str]:
        """Create a new API key for a user.

        Args:
            user_id: Owner user ID.
            name: Human-readable label for the key.

        Returns:
            Tuple of (APIKeyData, raw_key). The raw key is shown only once.

        Raises:
            ValueError: If user does not exist.
        """
        if user_id not in self._users:
            raise ValueError(f"User not found: {user_id}")

        raw_key = f"{settings.api_key_prefix}{secrets.token_hex(32)}"
        prefix = raw_key[: len(settings.api_key_prefix) + 8]
        key_hash = self._hash_key(raw_key)
        key_id = f"key_{uuid.uuid4().hex[:12]}"

        key_data = APIKeyData(
            key_id=key_id,
            user_id=user_id,
            name=name,
            prefix=prefix,
            key_hash=key_hash,
        )
        self._api_keys[key_id] = key_data
        self._key_hash_index[key_hash] = key_id
        logger.info("Created API key %s (prefix: %s) for user %s", key_id, prefix, user_id)
        return key_data, raw_key

    def verify_api_key(self, raw_key: str) -> APIKeyData | None:
        """Verify an API key and return its data if valid.

        Args:
            raw_key: The full API key from the Authorization header.

        Returns:
            APIKeyData if key is valid and active, None otherwise.
        """
        key_hash = self._hash_key(raw_key)
        key_id = self._key_hash_index.get(key_hash)
        if key_id is None:
            return None
        key_data = self._api_keys.get(key_id)
        if key_data is None or not key_data.is_active:
            return None
        return key_data

    def revoke_api_key(self, key_id: str, user_id: str) -> bool:
        """Revoke an API key.

        Args:
            key_id: The key to revoke.
            user_id: Must match the key's owner.

        Returns:
            True if revoked, False if not found or unauthorized.
        """
        key_data = self._api_keys.get(key_id)
        if key_data is None or key_data.user_id != user_id:
            return False
        key_data.is_active = False
        self._key_hash_index.pop(key_data.key_hash, None)
        logger.info("Revoked API key %s", key_id)
        return True

    def list_api_keys(self, user_id: str) -> list[APIKeyData]:
        """List all API keys for a user."""
        return [
            k for k in self._api_keys.values()
            if k.user_id == user_id
        ]


# Singleton instance
auth_service = AuthService()
