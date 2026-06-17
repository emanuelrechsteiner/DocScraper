"""Async SQLAlchemy repositories replacing in-memory singletons.

Each repository receives an ``AsyncSession`` and mirrors the public
API of the corresponding in-memory service, making the router
migration a straight substitution.
"""

from __future__ import annotations

import hashlib
import logging
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .models import APIKey, Job, UsageRecord, User

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# UserRepository
# ---------------------------------------------------------------------------


class UserRepository:
    """CRUD operations for the ``users`` table.

    Args:
        session: The async database session for this request.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self,
        email: str,
        name: Optional[str] = None,
        tier: str = "free",
    ) -> User:
        """Create a new user record.

        Args:
            email: Unique email address.
            name: Optional display name.
            tier: Billing tier string (default ``"free"``).

        Returns:
            The persisted ``User`` ORM object.

        Raises:
            ValueError: If a user with the same email already exists.
        """
        # Check for duplicate email before attempting insert so we can surface
        # a clear ValueError rather than an IntegrityError.
        existing = await self.get_by_email(email)
        if existing is not None:
            raise ValueError(f"Email already registered: {email}")

        user_id = f"user_{uuid.uuid4().hex[:12]}"
        user = User(
            user_id=user_id,
            email=email,
            name=name,
            tier=tier,
            created_at=datetime.now(timezone.utc),
        )
        self._session.add(user)
        try:
            await self._session.flush()
        except IntegrityError as exc:
            await self._session.rollback()
            raise ValueError(f"Email already registered: {email}") from exc

        logger.info("Created user %s (%s)", user_id, email)
        return user

    async def get_by_user_id(self, user_id: str) -> Optional[User]:
        """Return the user with the given public user_id, or ``None``."""
        result = await self._session.execute(
            select(User).where(User.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        """Return the user with the given email, or ``None``."""
        result = await self._session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def update(self, user_id: str, **kwargs: Any) -> Optional[User]:
        """Update allowed fields on a user record.

        Args:
            user_id: Public user identifier.
            **kwargs: Column names and their new values.

        Returns:
            Updated ``User`` object, or ``None`` if not found.
        """
        user = await self.get_by_user_id(user_id)
        if user is None:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        await self._session.flush()
        return user

    async def get_by_stripe_customer_id(
        self, customer_id: str
    ) -> Optional[User]:
        """Return the user associated with a Stripe customer ID, or ``None``."""
        result = await self._session.execute(
            select(User).where(User.stripe_customer_id == customer_id)
        )
        return result.scalar_one_or_none()

    async def get_by_clerk_user_id(self, clerk_user_id: str) -> Optional[User]:
        """Return the user with the given Clerk user ID, or ``None``."""
        result = await self._session.execute(
            select(User).where(User.clerk_user_id == clerk_user_id)
        )
        return result.scalar_one_or_none()

    async def get_or_create_by_clerk_id(
        self,
        clerk_user_id: str,
        email: str,
        name: Optional[str] = None,
        email_is_verified: bool = False,
    ) -> User:
        """Resolve a Clerk identity to a ``User``, creating it on first login.

        The account's stable identity is the (server-issued, signature-verified)
        ``clerk_user_id``, never the client-supplied email — this prevents
        account-squatting via a forged or unverified email claim.

        Account linking to a pre-existing email-based account happens *only* when
        the email is verified, preventing a hijack of an existing account.

        Args:
            clerk_user_id: Verified Clerk subject (``sub``) claim.
            email: Email to associate (a safe ``@clerk.local`` placeholder when
                the token carries no verified email).
            name: Optional display name.
            email_is_verified: Whether ``email`` came from a verified claim.

        Returns:
            The resolved ``User``.

        Raises:
            ValueError: If the verified email already belongs to a *different*
                Clerk identity (caller should surface this as HTTP 409).
        """
        user = await self.get_by_clerk_user_id(clerk_user_id)
        if user is not None:
            return user

        # Security invariant (enforced here, the data layer, not just the
        # caller): an unverified or missing email is NEVER stored or linked.
        # Fall back to a placeholder derived from the verified Clerk subject so
        # a forged email claim can never squat a real address.
        if not email_is_verified or not email or email.endswith("@clerk.local"):
            email = f"{clerk_user_id}@clerk.local"
            email_is_verified = False

        # Link to an existing account only via a verified, real email.
        if email_is_verified and not email.endswith("@clerk.local"):
            existing = await self.get_by_email(email)
            if existing is not None:
                if existing.clerk_user_id is None:
                    existing.clerk_user_id = clerk_user_id
                    await self._session.flush()
                    logger.info(
                        "Linked Clerk ID %s to existing user %s via verified email",
                        clerk_user_id,
                        existing.user_id,
                    )
                    return existing
                raise ValueError(
                    f"Email {email} already linked to a different account"
                )

        user_id = f"user_{uuid.uuid4().hex[:12]}"
        user = User(
            user_id=user_id,
            email=email,
            name=name,
            tier="free",
            clerk_user_id=clerk_user_id,
            created_at=datetime.now(timezone.utc),
        )
        self._session.add(user)
        try:
            await self._session.flush()
        except IntegrityError:
            # Concurrent first-login for the same Clerk ID — return the winner
            # rather than leaving a half-initialised row behind.
            await self._session.rollback()
            winner = await self.get_by_clerk_user_id(clerk_user_id)
            if winner is not None:
                return winner
            raise

        logger.info(
            "Auto-created user %s for Clerk ID %s", user_id, clerk_user_id
        )
        return user


# ---------------------------------------------------------------------------
# APIKeyRepository
# ---------------------------------------------------------------------------


class APIKeyRepository:
    """CRUD operations for the ``api_keys`` table.

    Args:
        session: The async database session for this request.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @staticmethod
    def _hash_key(raw_key: str) -> str:
        """Return a SHA-256 hex digest of *raw_key*.

        Args:
            raw_key: The plaintext API key string.

        Returns:
            64-character lowercase hex string.
        """
        return hashlib.sha256(raw_key.encode()).hexdigest()

    async def create(self, user_id: str, name: str) -> tuple[APIKey, str]:
        """Generate and persist a new API key.

        The full key is returned exactly once — only its SHA-256 hash is
        stored in the database.

        Args:
            user_id: Owner user_id (references ``users.user_id``).
            name: Human-readable key label.

        Returns:
            A tuple of (``APIKey`` ORM object, raw_key string).
        """
        raw_key = f"pk_{secrets.token_hex(32)}"
        prefix = raw_key[:12]  # "pk_" + first 8 hex chars
        key_hash = self._hash_key(raw_key)
        key_id = f"key_{uuid.uuid4().hex[:12]}"

        api_key = APIKey(
            key_id=key_id,
            user_id=user_id,
            name=name,
            prefix=prefix,
            key_hash=key_hash,
            is_active=True,
            created_at=datetime.now(timezone.utc),
        )
        self._session.add(api_key)
        await self._session.flush()

        logger.info(
            "Created API key %s (prefix: %s) for user %s", key_id, prefix, user_id
        )
        return api_key, raw_key

    async def verify(self, raw_key: str) -> Optional[APIKey]:
        """Verify a raw API key and return the active key record.

        Args:
            raw_key: The plaintext key from the ``Authorization`` header.

        Returns:
            ``APIKey`` if active and found, otherwise ``None``.
        """
        key_hash = self._hash_key(raw_key)
        result = await self._session.execute(
            select(APIKey).where(
                APIKey.key_hash == key_hash,
                APIKey.is_active.is_(True),
            )
        )
        return result.scalar_one_or_none()

    async def revoke(self, key_id: str, user_id: str) -> bool:
        """Deactivate an API key.

        Args:
            key_id: The public key identifier.
            user_id: Must match the key's owner to prevent cross-user revocation.

        Returns:
            ``True`` if the key was found and deactivated, ``False`` otherwise.
        """
        result = await self._session.execute(
            select(APIKey).where(
                APIKey.key_id == key_id,
                APIKey.user_id == user_id,
            )
        )
        api_key = result.scalar_one_or_none()
        if api_key is None:
            return False
        api_key.is_active = False
        await self._session.flush()
        logger.info("Revoked API key %s", key_id)
        return True

    async def list_for_user(self, user_id: str) -> list[APIKey]:
        """Return all API keys belonging to a user.

        Args:
            user_id: Owner user identifier.

        Returns:
            List of ``APIKey`` objects (may be empty).
        """
        result = await self._session.execute(
            select(APIKey).where(APIKey.user_id == user_id)
        )
        return list(result.scalars().all())


# ---------------------------------------------------------------------------
# JobRepository
# ---------------------------------------------------------------------------


class JobRepository:
    """CRUD operations for the ``jobs`` table.

    Args:
        session: The async database session for this request.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self,
        url: str,
        job_type: str = "scrape",
        max_pages: int = 100,
        output_format: str = "markdown",
        webhook_url: Optional[str] = None,
        owner_key_id: Optional[str] = None,
    ) -> Job:
        """Persist a new job record.

        Args:
            url: Target URL (scrape) or input directory path (process).
            job_type: ``"scrape"`` or ``"process"``.
            max_pages: Upper bound on pages to scrape.
            output_format: Desired output format string.
            webhook_url: Optional callback URL for completion events.
            owner_key_id: API key that submitted the job.

        Returns:
            The persisted ``Job`` ORM object with status ``"pending"``.
        """
        job_id = f"job_{uuid.uuid4().hex[:12]}"
        job = Job(
            job_id=job_id,
            status="pending",
            url=url,
            job_type=job_type,
            max_pages=max_pages,
            output_format=output_format,
            webhook_url=webhook_url,
            owner_key_id=owner_key_id,
            created_at=datetime.now(timezone.utc),
        )
        self._session.add(job)
        await self._session.flush()

        logger.info("Created %s job %s for %s", job_type, job_id, url)
        return job

    async def get(self, job_id: str) -> Optional[Job]:
        """Return the job with the given public job_id, or ``None``."""
        result = await self._session.execute(
            select(Job).where(Job.job_id == job_id)
        )
        return result.scalar_one_or_none()

    async def update(self, job_id: str, **kwargs: Any) -> Optional[Job]:
        """Update allowed fields on a job record.

        Args:
            job_id: Public job identifier.
            **kwargs: Column names and their new values.

        Returns:
            Updated ``Job`` object, or ``None`` if not found.
        """
        job = await self.get(job_id)
        if job is None:
            return None
        for key, value in kwargs.items():
            if hasattr(job, key):
                setattr(job, key, value)
        await self._session.flush()
        return job

    async def list_jobs(
        self,
        owner_key_id: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> tuple[list[Job], int]:
        """List jobs with optional filters and pagination.

        Args:
            owner_key_id: Filter to jobs owned by this API key.
            status: Filter to jobs with this status string.
            limit: Maximum rows to return.
            offset: Row offset for pagination.

        Returns:
            A tuple of ``(jobs, total_count)`` where ``total_count`` is
            the unfiltered count matching the filters (before pagination).
        """
        base_query = select(Job)
        count_query = select(func.count()).select_from(Job)

        if owner_key_id is not None:
            base_query = base_query.where(Job.owner_key_id == owner_key_id)
            count_query = count_query.where(Job.owner_key_id == owner_key_id)

        if status is not None:
            base_query = base_query.where(Job.status == status)
            count_query = count_query.where(Job.status == status)

        count_result = await self._session.execute(count_query)
        total = count_result.scalar_one()

        base_query = (
            base_query.order_by(Job.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        jobs_result = await self._session.execute(base_query)
        jobs = list(jobs_result.scalars().all())

        return jobs, total

    async def delete(self, job_id: str) -> bool:
        """Delete a job record.

        Args:
            job_id: Public job identifier.

        Returns:
            ``True`` if the job existed and was deleted, ``False`` otherwise.
        """
        job = await self.get(job_id)
        if job is None:
            return False
        await self._session.delete(job)
        await self._session.flush()
        return True


# ---------------------------------------------------------------------------
# UsageRepository
# ---------------------------------------------------------------------------


class UsageRepository:
    """Write and query operations for the ``usage_records`` table.

    Args:
        session: The async database session for this request.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def record(
        self,
        endpoint: str,
        method: str,
        status_code: int,
        response_time_ms: float,
        key_id: Optional[str] = None,
        pages_count: int = 0,
    ) -> UsageRecord:
        """Persist a single API usage event.

        Args:
            endpoint: API path that was called.
            method: HTTP method string (``"GET"``, ``"POST"``, etc.).
            status_code: HTTP response status code.
            response_time_ms: Request processing time in milliseconds.
            key_id: API key identifier if authenticated, otherwise ``None``.
            pages_count: Pages consumed by this request.

        Returns:
            The persisted ``UsageRecord`` ORM object.
        """
        record = UsageRecord(
            timestamp=datetime.now(timezone.utc),
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            response_time_ms=response_time_ms,
            key_id=key_id,
            pages_count=pages_count,
        )
        self._session.add(record)
        await self._session.flush()
        return record

    async def get_hourly_count(self, key_id: str) -> int:
        """Count usage records for *key_id* within the current UTC hour.

        Args:
            key_id: API key identifier.

        Returns:
            Integer count of records in the current clock hour.
        """
        now = datetime.now(timezone.utc)
        hour_start = now.replace(minute=0, second=0, microsecond=0)
        hour_end = hour_start + timedelta(hours=1)

        result = await self._session.execute(
            select(func.count()).select_from(UsageRecord).where(
                UsageRecord.key_id == key_id,
                UsageRecord.timestamp >= hour_start,
                UsageRecord.timestamp < hour_end,
            )
        )
        return result.scalar_one()

    async def get_daily_breakdown(
        self, key_id: str, days: int = 30
    ) -> list[dict[str, Any]]:
        """Aggregate usage records by calendar day for the past *days* days.

        Args:
            key_id: API key identifier.
            days: Number of calendar days to include (most recent first).

        Returns:
            List of dicts with keys ``date``, ``request_count``,
            ``pages_scraped``, ``errors``.
        """
        now = datetime.now(timezone.utc)
        results: list[dict[str, Any]] = []

        for i in range(days):
            day_start = (now - timedelta(days=i)).replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            day_end = day_start + timedelta(days=1)
            day_str = day_start.strftime("%Y-%m-%d")

            count_result = await self._session.execute(
                select(func.count()).select_from(UsageRecord).where(
                    UsageRecord.key_id == key_id,
                    UsageRecord.timestamp >= day_start,
                    UsageRecord.timestamp < day_end,
                )
            )
            request_count = count_result.scalar_one()

            pages_result = await self._session.execute(
                select(func.coalesce(func.sum(UsageRecord.pages_count), 0)).where(
                    UsageRecord.key_id == key_id,
                    UsageRecord.timestamp >= day_start,
                    UsageRecord.timestamp < day_end,
                )
            )
            pages_scraped = pages_result.scalar_one()

            errors_result = await self._session.execute(
                select(func.count()).select_from(UsageRecord).where(
                    UsageRecord.key_id == key_id,
                    UsageRecord.timestamp >= day_start,
                    UsageRecord.timestamp < day_end,
                    UsageRecord.status_code >= 400,
                )
            )
            errors = errors_result.scalar_one()

            results.append(
                {
                    "date": day_str,
                    "request_count": request_count,
                    "pages_scraped": int(pages_scraped),
                    "errors": errors,
                }
            )

        return results
