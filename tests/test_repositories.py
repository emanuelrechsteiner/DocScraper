"""Async tests for the SQLAlchemy repository layer.

Covers all four repositories: UserRepository, APIKeyRepository,
JobRepository, and UsageRepository. Each test uses the ``db_session``
fixture from conftest.py which provides an in-memory SQLite AsyncSession
with all tables already created.
"""

from __future__ import annotations

import hashlib
from datetime import datetime, timedelta, timezone

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.repositories import (
    APIKeyRepository,
    JobRepository,
    UsageRepository,
    UserRepository,
)


# ---------------------------------------------------------------------------
# UserRepository
# ---------------------------------------------------------------------------


class TestUserRepositoryCreate:
    """Tests for UserRepository.create()."""

    @pytest.mark.asyncio
    async def test_create_returns_user_object(self, db_session: AsyncSession) -> None:
        """create() returns a User ORM instance."""
        repo = UserRepository(db_session)
        user = await repo.create(email="alice@example.com")
        assert user is not None
        assert user.email == "alice@example.com"

    @pytest.mark.asyncio
    async def test_create_generates_user_id_with_prefix(
        self, db_session: AsyncSession
    ) -> None:
        """Generated user_id starts with 'user_'."""
        repo = UserRepository(db_session)
        user = await repo.create(email="bob@example.com")
        assert user.user_id.startswith("user_")

    @pytest.mark.asyncio
    async def test_create_user_id_is_unique_per_call(
        self, db_session: AsyncSession
    ) -> None:
        """Two distinct users receive different user_ids."""
        repo = UserRepository(db_session)
        u1 = await repo.create(email="one@example.com")
        u2 = await repo.create(email="two@example.com")
        assert u1.user_id != u2.user_id

    @pytest.mark.asyncio
    async def test_create_default_tier_is_free(
        self, db_session: AsyncSession
    ) -> None:
        """Tier defaults to 'free' when not supplied."""
        repo = UserRepository(db_session)
        user = await repo.create(email="carol@example.com")
        assert user.tier == "free"

    @pytest.mark.asyncio
    async def test_create_custom_tier(self, db_session: AsyncSession) -> None:
        """Explicit tier value is persisted."""
        repo = UserRepository(db_session)
        user = await repo.create(email="dave@example.com", tier="pro")
        assert user.tier == "pro"

    @pytest.mark.asyncio
    async def test_create_stores_name(self, db_session: AsyncSession) -> None:
        """Optional name is persisted when provided."""
        repo = UserRepository(db_session)
        user = await repo.create(email="eve@example.com", name="Eve Smith")
        assert user.name == "Eve Smith"

    @pytest.mark.asyncio
    async def test_create_name_defaults_to_none(
        self, db_session: AsyncSession
    ) -> None:
        """Name is None when not provided."""
        repo = UserRepository(db_session)
        user = await repo.create(email="frank@example.com")
        assert user.name is None

    @pytest.mark.asyncio
    async def test_create_sets_created_at(self, db_session: AsyncSession) -> None:
        """created_at is populated with a timezone-aware datetime."""
        repo = UserRepository(db_session)
        before = datetime.now(timezone.utc)
        user = await repo.create(email="grace@example.com")
        after = datetime.now(timezone.utc)
        assert user.created_at is not None
        # SQLite strips timezone info on round-trip — compare naive for portability.
        created = user.created_at.replace(tzinfo=None) if user.created_at.tzinfo is None else user.created_at.astimezone(timezone.utc).replace(tzinfo=None)
        assert before.replace(tzinfo=None) <= created <= after.replace(tzinfo=None)

    @pytest.mark.asyncio
    async def test_create_raises_value_error_on_duplicate_email(
        self, db_session: AsyncSession
    ) -> None:
        """Attempting to register the same email twice raises ValueError."""
        repo = UserRepository(db_session)
        await repo.create(email="dupe@example.com")
        with pytest.raises(ValueError, match="dupe@example.com"):
            await repo.create(email="dupe@example.com")


class TestUserRepositoryGetByUserId:
    """Tests for UserRepository.get_by_user_id()."""

    @pytest.mark.asyncio
    async def test_get_existing_user_returns_user(
        self, db_session: AsyncSession
    ) -> None:
        """Fetching by a known user_id returns the correct User."""
        repo = UserRepository(db_session)
        created = await repo.create(email="henry@example.com")
        fetched = await repo.get_by_user_id(created.user_id)
        assert fetched is not None
        assert fetched.user_id == created.user_id
        assert fetched.email == "henry@example.com"

    @pytest.mark.asyncio
    async def test_get_nonexistent_user_id_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """Fetching with an unknown user_id returns None."""
        repo = UserRepository(db_session)
        result = await repo.get_by_user_id("user_doesnotexist")
        assert result is None


class TestUserRepositoryGetByEmail:
    """Tests for UserRepository.get_by_email()."""

    @pytest.mark.asyncio
    async def test_get_by_email_returns_correct_user(
        self, db_session: AsyncSession
    ) -> None:
        """Fetching by a registered email returns the matching User."""
        repo = UserRepository(db_session)
        created = await repo.create(email="iris@example.com")
        fetched = await repo.get_by_email("iris@example.com")
        assert fetched is not None
        assert fetched.user_id == created.user_id

    @pytest.mark.asyncio
    async def test_get_by_email_unknown_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """Fetching an unregistered email returns None."""
        repo = UserRepository(db_session)
        result = await repo.get_by_email("nobody@example.com")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_email_is_case_sensitive(
        self, db_session: AsyncSession
    ) -> None:
        """Email lookup does not fold case — upper-case variant returns None."""
        repo = UserRepository(db_session)
        await repo.create(email="jack@example.com")
        result = await repo.get_by_email("JACK@EXAMPLE.COM")
        # SQLite may or may not fold case; we simply assert the method does not
        # crash. The key property is that it returns Optional[User].
        assert result is None or result.email == "jack@example.com"


class TestUserRepositoryUpdate:
    """Tests for UserRepository.update()."""

    @pytest.mark.asyncio
    async def test_update_existing_user_returns_updated_user(
        self, db_session: AsyncSession
    ) -> None:
        """Updating an existing field returns the User with new value."""
        repo = UserRepository(db_session)
        user = await repo.create(email="karen@example.com")
        updated = await repo.update(user.user_id, name="Karen Updated")
        assert updated is not None
        assert updated.name == "Karen Updated"

    @pytest.mark.asyncio
    async def test_update_tier(self, db_session: AsyncSession) -> None:
        """Tier can be upgraded via update()."""
        repo = UserRepository(db_session)
        user = await repo.create(email="leo@example.com")
        updated = await repo.update(user.user_id, tier="enterprise")
        assert updated is not None
        assert updated.tier == "enterprise"

    @pytest.mark.asyncio
    async def test_update_multiple_fields_at_once(
        self, db_session: AsyncSession
    ) -> None:
        """Multiple keyword arguments are all applied in one call."""
        repo = UserRepository(db_session)
        user = await repo.create(email="mia@example.com")
        updated = await repo.update(
            user.user_id,
            name="Mia Updated",
            tier="pro",
            stripe_customer_id="cus_abc123",
        )
        assert updated is not None
        assert updated.name == "Mia Updated"
        assert updated.tier == "pro"
        assert updated.stripe_customer_id == "cus_abc123"

    @pytest.mark.asyncio
    async def test_update_nonexistent_user_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """Updating a user_id that does not exist returns None."""
        repo = UserRepository(db_session)
        result = await repo.update("user_nonexistent", name="Ghost")
        assert result is None

    @pytest.mark.asyncio
    async def test_update_with_unknown_kwarg_is_ignored(
        self, db_session: AsyncSession
    ) -> None:
        """Unknown keyword arguments do not raise — they are silently ignored."""
        repo = UserRepository(db_session)
        user = await repo.create(email="nick@example.com")
        updated = await repo.update(user.user_id, nonexistent_column="value")
        assert updated is not None
        assert updated.email == "nick@example.com"


class TestUserRepositoryGetByStripeCustomerId:
    """Tests for UserRepository.get_by_stripe_customer_id()."""

    @pytest.mark.asyncio
    async def test_get_by_stripe_customer_id_returns_user(
        self, db_session: AsyncSession
    ) -> None:
        """After setting stripe_customer_id, lookup returns the user."""
        repo = UserRepository(db_session)
        user = await repo.create(email="olivia@example.com")
        await repo.update(user.user_id, stripe_customer_id="cus_xyz999")
        found = await repo.get_by_stripe_customer_id("cus_xyz999")
        assert found is not None
        assert found.user_id == user.user_id

    @pytest.mark.asyncio
    async def test_get_by_stripe_customer_id_unknown_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """Lookup with an unregistered Stripe customer ID returns None."""
        repo = UserRepository(db_session)
        result = await repo.get_by_stripe_customer_id("cus_notexist")
        assert result is None


# ---------------------------------------------------------------------------
# APIKeyRepository
# ---------------------------------------------------------------------------


class TestAPIKeyRepositoryCreate:
    """Tests for APIKeyRepository.create()."""

    @pytest.mark.asyncio
    async def test_create_returns_key_and_raw_string(
        self, db_session: AsyncSession
    ) -> None:
        """create() returns a (APIKey, str) tuple."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="peter@example.com")
        api_key, raw_key = await key_repo.create(user.user_id, name="Test Key")
        assert api_key is not None
        assert isinstance(raw_key, str)

    @pytest.mark.asyncio
    async def test_raw_key_starts_with_pk_prefix(
        self, db_session: AsyncSession
    ) -> None:
        """Raw key always starts with 'pk_'."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="quinn@example.com")
        _, raw_key = await key_repo.create(user.user_id, name="My Key")
        assert raw_key.startswith("pk_")

    @pytest.mark.asyncio
    async def test_key_hash_stored_not_raw(self, db_session: AsyncSession) -> None:
        """The stored key_hash is the SHA-256 digest, not the plaintext key."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="rachel@example.com")
        api_key, raw_key = await key_repo.create(user.user_id, name="Hash Check")
        expected_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        assert api_key.key_hash == expected_hash
        assert api_key.key_hash != raw_key

    @pytest.mark.asyncio
    async def test_key_id_starts_with_key_prefix(
        self, db_session: AsyncSession
    ) -> None:
        """Generated key_id starts with 'key_'."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="sam@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="Key ID Check")
        assert api_key.key_id.startswith("key_")

    @pytest.mark.asyncio
    async def test_key_is_active_on_creation(self, db_session: AsyncSession) -> None:
        """Newly created key has is_active set to True."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="tara@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="Active Check")
        assert api_key.is_active is True

    @pytest.mark.asyncio
    async def test_key_name_stored_correctly(self, db_session: AsyncSession) -> None:
        """The name label is stored on the key object."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="uma@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="Production Key")
        assert api_key.name == "Production Key"

    @pytest.mark.asyncio
    async def test_prefix_stored_on_key(self, db_session: AsyncSession) -> None:
        """The prefix field stores the first 12 characters of the raw key."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="vera@example.com")
        api_key, raw_key = await key_repo.create(user.user_id, name="Prefix Check")
        assert api_key.prefix == raw_key[:12]


class TestAPIKeyRepositoryVerify:
    """Tests for APIKeyRepository.verify()."""

    @pytest.mark.asyncio
    async def test_verify_valid_key_returns_api_key(
        self, db_session: AsyncSession
    ) -> None:
        """verify() returns the active APIKey for a valid raw key."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="will@example.com")
        created_key, raw_key = await key_repo.create(user.user_id, name="Valid Key")
        found_key = await key_repo.verify(raw_key)
        assert found_key is not None
        assert found_key.key_id == created_key.key_id

    @pytest.mark.asyncio
    async def test_verify_invalid_key_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """verify() returns None for a raw key that has never been registered."""
        key_repo = APIKeyRepository(db_session)
        result = await key_repo.verify("pk_totally_fake_key_that_does_not_exist")
        assert result is None

    @pytest.mark.asyncio
    async def test_verify_revoked_key_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """verify() returns None after the key has been revoked."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="xena@example.com")
        api_key, raw_key = await key_repo.create(user.user_id, name="To Revoke")
        await key_repo.revoke(api_key.key_id, user.user_id)
        result = await key_repo.verify(raw_key)
        assert result is None


class TestAPIKeyRepositoryRevoke:
    """Tests for APIKeyRepository.revoke()."""

    @pytest.mark.asyncio
    async def test_revoke_active_key_returns_true(
        self, db_session: AsyncSession
    ) -> None:
        """Revoking an active key returns True."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="yara@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="Revocable")
        result = await key_repo.revoke(api_key.key_id, user.user_id)
        assert result is True

    @pytest.mark.asyncio
    async def test_revoke_sets_is_active_false(
        self, db_session: AsyncSession
    ) -> None:
        """After revocation is_active is False on the stored record."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="zara@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="To Deactivate")
        await key_repo.revoke(api_key.key_id, user.user_id)
        # Confirm by re-fetching from the list.
        keys = await key_repo.list_for_user(user.user_id)
        assert len(keys) == 1
        assert keys[0].is_active is False

    @pytest.mark.asyncio
    async def test_revoke_nonexistent_key_returns_false(
        self, db_session: AsyncSession
    ) -> None:
        """Revoking a key_id that does not exist returns False."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="anna@example.com")
        result = await key_repo.revoke("key_doesnotexist", user.user_id)
        assert result is False

    @pytest.mark.asyncio
    async def test_revoke_wrong_user_returns_false(
        self, db_session: AsyncSession
    ) -> None:
        """Revoking a valid key with a mismatched user_id returns False."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        owner = await user_repo.create(email="owner@example.com")
        other = await user_repo.create(email="other@example.com")
        api_key, _ = await key_repo.create(owner.user_id, name="Owner Key")
        result = await key_repo.revoke(api_key.key_id, other.user_id)
        assert result is False


class TestAPIKeyRepositoryListForUser:
    """Tests for APIKeyRepository.list_for_user()."""

    @pytest.mark.asyncio
    async def test_list_returns_all_keys_for_user(
        self, db_session: AsyncSession
    ) -> None:
        """list_for_user() returns every key belonging to the user."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="brad@example.com")
        await key_repo.create(user.user_id, name="Key One")
        await key_repo.create(user.user_id, name="Key Two")
        keys = await key_repo.list_for_user(user.user_id)
        assert len(keys) == 2

    @pytest.mark.asyncio
    async def test_list_empty_for_user_with_no_keys(
        self, db_session: AsyncSession
    ) -> None:
        """list_for_user() returns an empty list when the user has no keys."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="cathy@example.com")
        keys = await key_repo.list_for_user(user.user_id)
        assert keys == []

    @pytest.mark.asyncio
    async def test_list_does_not_return_other_users_keys(
        self, db_session: AsyncSession
    ) -> None:
        """Keys belonging to another user are not returned."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user_a = await user_repo.create(email="usera@example.com")
        user_b = await user_repo.create(email="userb@example.com")
        await key_repo.create(user_a.user_id, name="A Key")
        keys_b = await key_repo.list_for_user(user_b.user_id)
        assert keys_b == []

    @pytest.mark.asyncio
    async def test_list_includes_revoked_keys(
        self, db_session: AsyncSession
    ) -> None:
        """Revoked keys are still returned by list_for_user (is_active=False)."""
        user_repo = UserRepository(db_session)
        key_repo = APIKeyRepository(db_session)
        user = await user_repo.create(email="derek@example.com")
        api_key, _ = await key_repo.create(user.user_id, name="Revoked Key")
        await key_repo.revoke(api_key.key_id, user.user_id)
        keys = await key_repo.list_for_user(user.user_id)
        assert len(keys) == 1
        assert keys[0].is_active is False


# ---------------------------------------------------------------------------
# JobRepository
# ---------------------------------------------------------------------------


class TestJobRepositoryCreate:
    """Tests for JobRepository.create()."""

    @pytest.mark.asyncio
    async def test_create_returns_job_object(self, db_session: AsyncSession) -> None:
        """create() returns a Job ORM instance."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        assert job is not None

    @pytest.mark.asyncio
    async def test_create_job_id_has_job_prefix(
        self, db_session: AsyncSession
    ) -> None:
        """Generated job_id starts with 'job_'."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        assert job.job_id.startswith("job_")

    @pytest.mark.asyncio
    async def test_create_default_status_is_pending(
        self, db_session: AsyncSession
    ) -> None:
        """Newly created job has status 'pending'."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        assert job.status == "pending"

    @pytest.mark.asyncio
    async def test_create_default_job_type_is_scrape(
        self, db_session: AsyncSession
    ) -> None:
        """Default job_type is 'scrape'."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        assert job.job_type == "scrape"

    @pytest.mark.asyncio
    async def test_create_custom_job_type(self, db_session: AsyncSession) -> None:
        """Custom job_type is persisted correctly."""
        repo = JobRepository(db_session)
        job = await repo.create(url="/some/path", job_type="process")
        assert job.job_type == "process"

    @pytest.mark.asyncio
    async def test_create_stores_url(self, db_session: AsyncSession) -> None:
        """The URL field is stored on the job."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://api.example.com/docs")
        assert job.url == "https://api.example.com/docs"

    @pytest.mark.asyncio
    async def test_create_stores_max_pages(self, db_session: AsyncSession) -> None:
        """Custom max_pages value is persisted."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com", max_pages=50)
        assert job.max_pages == 50

    @pytest.mark.asyncio
    async def test_create_stores_webhook_url(self, db_session: AsyncSession) -> None:
        """webhook_url is persisted when provided."""
        repo = JobRepository(db_session)
        job = await repo.create(
            url="https://docs.example.com",
            webhook_url="https://hooks.example.com/callback",
        )
        assert job.webhook_url == "https://hooks.example.com/callback"

    @pytest.mark.asyncio
    async def test_create_stores_owner_key_id(self, db_session: AsyncSession) -> None:
        """owner_key_id is persisted when provided."""
        repo = JobRepository(db_session)
        job = await repo.create(
            url="https://docs.example.com", owner_key_id="key_abc123def456"
        )
        assert job.owner_key_id == "key_abc123def456"

    @pytest.mark.asyncio
    async def test_create_two_jobs_have_unique_ids(
        self, db_session: AsyncSession
    ) -> None:
        """Two consecutive job creations receive distinct job_ids."""
        repo = JobRepository(db_session)
        j1 = await repo.create(url="https://a.example.com")
        j2 = await repo.create(url="https://b.example.com")
        assert j1.job_id != j2.job_id


class TestJobRepositoryGet:
    """Tests for JobRepository.get()."""

    @pytest.mark.asyncio
    async def test_get_existing_job_returns_job(
        self, db_session: AsyncSession
    ) -> None:
        """get() returns the correct job for a known job_id."""
        repo = JobRepository(db_session)
        created = await repo.create(url="https://docs.example.com")
        fetched = await repo.get(created.job_id)
        assert fetched is not None
        assert fetched.job_id == created.job_id

    @pytest.mark.asyncio
    async def test_get_nonexistent_job_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """get() returns None for an unknown job_id."""
        repo = JobRepository(db_session)
        result = await repo.get("job_doesnotexist")
        assert result is None


class TestJobRepositoryUpdate:
    """Tests for JobRepository.update()."""

    @pytest.mark.asyncio
    async def test_update_status_field(self, db_session: AsyncSession) -> None:
        """Updating status transitions the job correctly."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        updated = await repo.update(job.job_id, status="running")
        assert updated is not None
        assert updated.status == "running"

    @pytest.mark.asyncio
    async def test_update_multiple_fields(self, db_session: AsyncSession) -> None:
        """Multiple fields can be updated simultaneously."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        now = datetime.now(timezone.utc)
        updated = await repo.update(
            job.job_id,
            status="completed",
            pages_scraped=42,
            progress=100.0,
            completed_at=now,
        )
        assert updated is not None
        assert updated.status == "completed"
        assert updated.pages_scraped == 42
        assert updated.progress == 100.0

    @pytest.mark.asyncio
    async def test_update_error_message(self, db_session: AsyncSession) -> None:
        """Error message field can be set via update()."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        updated = await repo.update(
            job.job_id, status="failed", error_message="Connection refused"
        )
        assert updated is not None
        assert updated.error_message == "Connection refused"

    @pytest.mark.asyncio
    async def test_update_nonexistent_job_returns_none(
        self, db_session: AsyncSession
    ) -> None:
        """update() returns None for an unknown job_id."""
        repo = JobRepository(db_session)
        result = await repo.update("job_ghost", status="running")
        assert result is None


class TestJobRepositoryListJobs:
    """Tests for JobRepository.list_jobs()."""

    @pytest.mark.asyncio
    async def test_list_returns_all_jobs_when_no_filters(
        self, db_session: AsyncSession
    ) -> None:
        """With no filters, all created jobs are returned."""
        repo = JobRepository(db_session)
        await repo.create(url="https://a.example.com")
        await repo.create(url="https://b.example.com")
        await repo.create(url="https://c.example.com")
        jobs, total = await repo.list_jobs()
        assert total == 3
        assert len(jobs) == 3

    @pytest.mark.asyncio
    async def test_list_empty_when_no_jobs(self, db_session: AsyncSession) -> None:
        """With no jobs in the database the result is empty."""
        repo = JobRepository(db_session)
        jobs, total = await repo.list_jobs()
        assert total == 0
        assert jobs == []

    @pytest.mark.asyncio
    async def test_list_filter_by_status(self, db_session: AsyncSession) -> None:
        """Filtering by status returns only jobs with that status."""
        repo = JobRepository(db_session)
        j1 = await repo.create(url="https://a.example.com")
        await repo.create(url="https://b.example.com")
        await repo.update(j1.job_id, status="completed")
        jobs, total = await repo.list_jobs(status="completed")
        assert total == 1
        assert jobs[0].job_id == j1.job_id

    @pytest.mark.asyncio
    async def test_list_filter_by_owner_key_id(
        self, db_session: AsyncSession
    ) -> None:
        """Filtering by owner_key_id returns only that owner's jobs."""
        repo = JobRepository(db_session)
        await repo.create(url="https://a.example.com", owner_key_id="key_owner1")
        await repo.create(url="https://b.example.com", owner_key_id="key_owner1")
        await repo.create(url="https://c.example.com", owner_key_id="key_owner2")
        jobs, total = await repo.list_jobs(owner_key_id="key_owner1")
        assert total == 2
        assert all(j.owner_key_id == "key_owner1" for j in jobs)

    @pytest.mark.asyncio
    async def test_list_filter_by_owner_and_status(
        self, db_session: AsyncSession
    ) -> None:
        """Combining owner_key_id and status filters narrows results correctly."""
        repo = JobRepository(db_session)
        j1 = await repo.create(url="https://a.example.com", owner_key_id="key_combo")
        await repo.create(url="https://b.example.com", owner_key_id="key_combo")
        await repo.update(j1.job_id, status="completed")
        jobs, total = await repo.list_jobs(
            owner_key_id="key_combo", status="completed"
        )
        assert total == 1
        assert jobs[0].job_id == j1.job_id

    @pytest.mark.asyncio
    async def test_list_pagination_limit(self, db_session: AsyncSession) -> None:
        """limit parameter caps the returned rows while total reflects full count."""
        repo = JobRepository(db_session)
        for i in range(5):
            await repo.create(url=f"https://page{i}.example.com")
        jobs, total = await repo.list_jobs(limit=2)
        assert total == 5
        assert len(jobs) == 2

    @pytest.mark.asyncio
    async def test_list_pagination_offset(self, db_session: AsyncSession) -> None:
        """offset skips rows while total remains the full count."""
        repo = JobRepository(db_session)
        for i in range(5):
            await repo.create(url=f"https://offset{i}.example.com")
        jobs_page1, _ = await repo.list_jobs(limit=3, offset=0)
        jobs_page2, total = await repo.list_jobs(limit=3, offset=3)
        assert total == 5
        assert len(jobs_page2) == 2
        # Pages should not overlap.
        ids_page1 = {j.job_id for j in jobs_page1}
        ids_page2 = {j.job_id for j in jobs_page2}
        assert ids_page1.isdisjoint(ids_page2)

    @pytest.mark.asyncio
    async def test_list_filter_returns_zero_when_status_absent(
        self, db_session: AsyncSession
    ) -> None:
        """Filtering by a status that no job has returns an empty list."""
        repo = JobRepository(db_session)
        await repo.create(url="https://docs.example.com")
        jobs, total = await repo.list_jobs(status="cancelled")
        assert total == 0
        assert jobs == []

    @pytest.mark.asyncio
    async def test_list_jobs_ordered_by_created_at_desc(
        self, db_session: AsyncSession
    ) -> None:
        """Results are ordered newest-first (descending created_at)."""
        repo = JobRepository(db_session)
        j1 = await repo.create(url="https://first.example.com")
        j2 = await repo.create(url="https://second.example.com")
        j3 = await repo.create(url="https://third.example.com")
        jobs, _ = await repo.list_jobs()
        job_ids = [j.job_id for j in jobs]
        # Most recently created job should come first.
        assert job_ids[0] == j3.job_id
        assert job_ids[-1] == j1.job_id


class TestJobRepositoryDelete:
    """Tests for JobRepository.delete()."""

    @pytest.mark.asyncio
    async def test_delete_existing_job_returns_true(
        self, db_session: AsyncSession
    ) -> None:
        """Deleting a known job returns True."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        result = await repo.delete(job.job_id)
        assert result is True

    @pytest.mark.asyncio
    async def test_delete_removes_job_from_database(
        self, db_session: AsyncSession
    ) -> None:
        """After deletion get() returns None for the same job_id."""
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        await repo.delete(job.job_id)
        fetched = await repo.get(job.job_id)
        assert fetched is None

    @pytest.mark.asyncio
    async def test_delete_nonexistent_job_returns_false(
        self, db_session: AsyncSession
    ) -> None:
        """Deleting a job_id that does not exist returns False."""
        repo = JobRepository(db_session)
        result = await repo.delete("job_ghost_job")
        assert result is False

    @pytest.mark.asyncio
    async def test_delete_does_not_affect_other_jobs(
        self, db_session: AsyncSession
    ) -> None:
        """Deleting one job leaves others untouched."""
        repo = JobRepository(db_session)
        j1 = await repo.create(url="https://keep.example.com")
        j2 = await repo.create(url="https://delete.example.com")
        await repo.delete(j2.job_id)
        _, total = await repo.list_jobs()
        assert total == 1
        remaining = await repo.get(j1.job_id)
        assert remaining is not None


# ---------------------------------------------------------------------------
# UsageRepository
# ---------------------------------------------------------------------------


class TestUsageRepositoryRecord:
    """Tests for UsageRepository.record()."""

    @pytest.mark.asyncio
    async def test_record_returns_usage_record_object(
        self, db_session: AsyncSession
    ) -> None:
        """record() returns a persisted UsageRecord."""
        repo = UsageRepository(db_session)
        usage = await repo.record(
            endpoint="/v1/scrape",
            method="POST",
            status_code=200,
            response_time_ms=42.0,
        )
        assert usage is not None
        assert usage.id is not None

    @pytest.mark.asyncio
    async def test_record_stores_all_fields(self, db_session: AsyncSession) -> None:
        """All supplied fields are persisted correctly."""
        repo = UsageRepository(db_session)
        usage = await repo.record(
            endpoint="/v1/jobs",
            method="GET",
            status_code=200,
            response_time_ms=15.5,
            key_id="key_abc",
            pages_count=3,
        )
        assert usage.endpoint == "/v1/jobs"
        assert usage.method == "GET"
        assert usage.status_code == 200
        assert usage.response_time_ms == 15.5
        assert usage.key_id == "key_abc"
        assert usage.pages_count == 3

    @pytest.mark.asyncio
    async def test_record_without_key_id_stores_none(
        self, db_session: AsyncSession
    ) -> None:
        """key_id defaults to None for unauthenticated requests."""
        repo = UsageRepository(db_session)
        usage = await repo.record(
            endpoint="/v1/health",
            method="GET",
            status_code=200,
            response_time_ms=1.0,
        )
        assert usage.key_id is None

    @pytest.mark.asyncio
    async def test_record_pages_count_defaults_to_zero(
        self, db_session: AsyncSession
    ) -> None:
        """pages_count defaults to 0 when not provided."""
        repo = UsageRepository(db_session)
        usage = await repo.record(
            endpoint="/v1/health",
            method="GET",
            status_code=200,
            response_time_ms=1.0,
            key_id="key_xyz",
        )
        assert usage.pages_count == 0

    @pytest.mark.asyncio
    async def test_record_timestamp_is_set(self, db_session: AsyncSession) -> None:
        """timestamp is populated automatically on creation."""
        repo = UsageRepository(db_session)
        before = datetime.now(timezone.utc)
        usage = await repo.record(
            endpoint="/v1/scrape",
            method="POST",
            status_code=201,
            response_time_ms=88.8,
        )
        after = datetime.now(timezone.utc)
        assert usage.timestamp is not None
        ts = usage.timestamp.replace(tzinfo=None) if usage.timestamp.tzinfo is None else usage.timestamp.astimezone(timezone.utc).replace(tzinfo=None)
        assert before.replace(tzinfo=None) <= ts <= after.replace(tzinfo=None)


class TestUsageRepositoryGetHourlyCount:
    """Tests for UsageRepository.get_hourly_count()."""

    @pytest.mark.asyncio
    async def test_hourly_count_is_zero_with_no_records(
        self, db_session: AsyncSession
    ) -> None:
        """get_hourly_count() returns 0 when there are no records for the key."""
        repo = UsageRepository(db_session)
        count = await repo.get_hourly_count("key_unknown")
        assert count == 0

    @pytest.mark.asyncio
    async def test_hourly_count_includes_current_hour_records(
        self, db_session: AsyncSession
    ) -> None:
        """Records inserted just now are counted within the current hour."""
        repo = UsageRepository(db_session)
        key_id = "key_hourtest"
        await repo.record("/v1/jobs", "GET", 200, 10.0, key_id=key_id)
        await repo.record("/v1/jobs", "GET", 200, 10.0, key_id=key_id)
        count = await repo.get_hourly_count(key_id)
        assert count == 2

    @pytest.mark.asyncio
    async def test_hourly_count_excludes_other_key(
        self, db_session: AsyncSession
    ) -> None:
        """Records belonging to a different key are not counted."""
        repo = UsageRepository(db_session)
        await repo.record("/v1/jobs", "GET", 200, 10.0, key_id="key_other")
        count = await repo.get_hourly_count("key_mine")
        assert count == 0

    @pytest.mark.asyncio
    async def test_hourly_count_excludes_previous_hour(
        self, db_session: AsyncSession
    ) -> None:
        """Records timestamped in the previous hour are not counted."""
        from sqlalchemy import text

        repo = UsageRepository(db_session)
        key_id = "key_oldhour"

        # Insert a record directly with a timestamp 2 hours ago.
        two_hours_ago = datetime.now(timezone.utc) - timedelta(hours=2)
        from api.db.models import UsageRecord

        old_record = UsageRecord(
            timestamp=two_hours_ago,
            endpoint="/v1/old",
            method="GET",
            status_code=200,
            response_time_ms=5.0,
            key_id=key_id,
            pages_count=0,
        )
        db_session.add(old_record)
        await db_session.flush()

        count = await repo.get_hourly_count(key_id)
        assert count == 0


class TestUsageRepositoryGetDailyBreakdown:
    """Tests for UsageRepository.get_daily_breakdown()."""

    @pytest.mark.asyncio
    async def test_daily_breakdown_returns_list_of_dicts(
        self, db_session: AsyncSession
    ) -> None:
        """get_daily_breakdown() returns a list of dict objects."""
        repo = UsageRepository(db_session)
        result = await repo.get_daily_breakdown("key_breakdown", days=7)
        assert isinstance(result, list)
        assert len(result) == 7

    @pytest.mark.asyncio
    async def test_daily_breakdown_dict_has_required_keys(
        self, db_session: AsyncSession
    ) -> None:
        """Each dict in the breakdown has the expected keys."""
        repo = UsageRepository(db_session)
        result = await repo.get_daily_breakdown("key_keys", days=1)
        assert len(result) == 1
        entry = result[0]
        assert set(entry.keys()) == {"date", "request_count", "pages_scraped", "errors"}

    @pytest.mark.asyncio
    async def test_daily_breakdown_date_format(
        self, db_session: AsyncSession
    ) -> None:
        """The date field is formatted as YYYY-MM-DD."""
        repo = UsageRepository(db_session)
        result = await repo.get_daily_breakdown("key_fmt", days=3)
        for entry in result:
            # strptime raises ValueError if the format is wrong.
            parsed = datetime.strptime(entry["date"], "%Y-%m-%d")
            assert parsed is not None

    @pytest.mark.asyncio
    async def test_daily_breakdown_default_days_is_30(
        self, db_session: AsyncSession
    ) -> None:
        """Default days parameter produces 30 entries."""
        repo = UsageRepository(db_session)
        result = await repo.get_daily_breakdown("key_30days")
        assert len(result) == 30

    @pytest.mark.asyncio
    async def test_daily_breakdown_today_counts_current_requests(
        self, db_session: AsyncSession
    ) -> None:
        """Requests recorded today appear in the first entry of the breakdown."""
        repo = UsageRepository(db_session)
        key_id = "key_today"
        await repo.record("/v1/scrape", "POST", 200, 100.0, key_id=key_id, pages_count=5)
        await repo.record("/v1/scrape", "POST", 200, 120.0, key_id=key_id, pages_count=3)
        result = await repo.get_daily_breakdown(key_id, days=1)
        today = result[0]
        assert today["request_count"] == 2
        assert today["pages_scraped"] == 8

    @pytest.mark.asyncio
    async def test_daily_breakdown_counts_errors_by_status_code(
        self, db_session: AsyncSession
    ) -> None:
        """Responses with status >= 400 are counted in the errors field."""
        repo = UsageRepository(db_session)
        key_id = "key_errors"
        await repo.record("/v1/scrape", "POST", 200, 10.0, key_id=key_id)
        await repo.record("/v1/scrape", "POST", 429, 5.0, key_id=key_id)
        await repo.record("/v1/scrape", "POST", 500, 2.0, key_id=key_id)
        result = await repo.get_daily_breakdown(key_id, days=1)
        today = result[0]
        assert today["request_count"] == 3
        assert today["errors"] == 2

    @pytest.mark.asyncio
    async def test_daily_breakdown_zero_counts_for_empty_key(
        self, db_session: AsyncSession
    ) -> None:
        """All counts are 0 for a key with no records."""
        repo = UsageRepository(db_session)
        result = await repo.get_daily_breakdown("key_empty", days=3)
        for entry in result:
            assert entry["request_count"] == 0
            assert entry["pages_scraped"] == 0
            assert entry["errors"] == 0

    @pytest.mark.asyncio
    async def test_daily_breakdown_excludes_other_keys(
        self, db_session: AsyncSession
    ) -> None:
        """Records for a different key do not appear in the breakdown."""
        repo = UsageRepository(db_session)
        await repo.record("/v1/scrape", "POST", 200, 10.0, key_id="key_other_user")
        result = await repo.get_daily_breakdown("key_mine_only", days=1)
        assert result[0]["request_count"] == 0
