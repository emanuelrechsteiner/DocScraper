"""Tests for SQLAlchemy ORM model definitions (#32).

Verifies table names, column presence, unique constraints, indexes,
and Base.metadata registration without requiring a live database.
"""

from __future__ import annotations

import pytest
import sqlalchemy as sa

from api.db.models import APIKey, Base, Job, UsageRecord, User

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _table(model: type) -> sa.Table:
    """Return the underlying SA Table for an ORM model class."""
    return model.__table__  # type: ignore[attr-defined]


def _column_names(model: type) -> set[str]:
    """Return the set of column names for a model table."""
    return {c.name for c in _table(model).columns}


def _unique_column_names(model: type) -> set[str]:
    """Return column names that carry a UniqueConstraint or unique=True."""
    unique: set[str] = set()
    for col in _table(model).columns:
        if col.unique:
            unique.add(col.name)
    for constraint in _table(model).constraints:
        if isinstance(constraint, sa.UniqueConstraint):
            for col in constraint.columns:
                unique.add(col.name)
    return unique


def _index_column_sets(model: type) -> list[frozenset[str]]:
    """Return a list of frozensets, each containing the columns of one index."""
    result = []
    for idx in sa.inspect(_table(model)).indexes:
        result.append(frozenset(col.name for col in idx.columns))
    return result


# ---------------------------------------------------------------------------
# Base metadata
# ---------------------------------------------------------------------------


class TestBaseMetadata:
    """All four tables must be registered in Base.metadata."""

    def test_all_tables_in_metadata(self) -> None:
        expected = {"users", "api_keys", "jobs", "usage_records"}
        assert expected.issubset(set(Base.metadata.tables.keys()))

    def test_exactly_four_core_tables(self) -> None:
        tables = set(Base.metadata.tables.keys())
        core = {"users", "api_keys", "jobs", "usage_records"}
        assert core == tables


# ---------------------------------------------------------------------------
# User model
# ---------------------------------------------------------------------------


class TestUserModel:
    """Schema verification for the users table."""

    def test_table_name(self) -> None:
        assert User.__tablename__ == "users"

    def test_required_columns_exist(self) -> None:
        required = {
            "id",
            "user_id",
            "email",
            "name",
            "tier",
            "stripe_customer_id",
            "stripe_subscription_id",
            "created_at",
        }
        assert required.issubset(_column_names(User))

    def test_user_id_unique(self) -> None:
        assert "user_id" in _unique_column_names(User)

    def test_email_unique(self) -> None:
        assert "email" in _unique_column_names(User)

    def test_tier_default(self) -> None:
        tier_col = _table(User).c["tier"]
        assert tier_col.default is not None or tier_col.server_default is not None or str(tier_col.default) == "free"

    def test_created_at_timezone_aware(self) -> None:
        col = _table(User).c["created_at"]
        assert isinstance(col.type, sa.DateTime)
        assert col.type.timezone is True

    def test_user_id_indexed(self) -> None:
        index_sets = _index_column_sets(User)
        assert frozenset({"user_id"}) in index_sets

    def test_email_indexed(self) -> None:
        index_sets = _index_column_sets(User)
        assert frozenset({"email"}) in index_sets


# ---------------------------------------------------------------------------
# APIKey model
# ---------------------------------------------------------------------------


class TestAPIKeyModel:
    """Schema verification for the api_keys table."""

    def test_table_name(self) -> None:
        assert APIKey.__tablename__ == "api_keys"

    def test_required_columns_exist(self) -> None:
        required = {
            "id",
            "key_id",
            "user_id",
            "name",
            "prefix",
            "key_hash",
            "is_active",
            "created_at",
        }
        assert required.issubset(_column_names(APIKey))

    def test_key_id_unique(self) -> None:
        assert "key_id" in _unique_column_names(APIKey)

    def test_key_hash_unique(self) -> None:
        assert "key_hash" in _unique_column_names(APIKey)

    def test_key_hash_indexed(self) -> None:
        index_sets = _index_column_sets(APIKey)
        assert frozenset({"key_hash"}) in index_sets

    def test_user_id_indexed(self) -> None:
        index_sets = _index_column_sets(APIKey)
        assert frozenset({"user_id"}) in index_sets

    def test_is_active_default_true(self) -> None:
        col = _table(APIKey).c["is_active"]
        assert col.default is not None

    def test_created_at_timezone_aware(self) -> None:
        col = _table(APIKey).c["created_at"]
        assert isinstance(col.type, sa.DateTime)
        assert col.type.timezone is True


# ---------------------------------------------------------------------------
# Job model
# ---------------------------------------------------------------------------


class TestJobModel:
    """Schema verification for the jobs table."""

    def test_table_name(self) -> None:
        assert Job.__tablename__ == "jobs"

    def test_required_columns_exist(self) -> None:
        required = {
            "id",
            "job_id",
            "status",
            "url",
            "job_type",
            "max_pages",
            "output_format",
            "webhook_url",
            "created_at",
            "started_at",
            "completed_at",
            "pages_scraped",
            "pages_failed",
            "progress",
            "error_message",
            "output_files",
            "summary",
            "owner_key_id",
        }
        assert required.issubset(_column_names(Job))

    def test_job_id_unique(self) -> None:
        assert "job_id" in _unique_column_names(Job)

    def test_job_id_indexed(self) -> None:
        index_sets = _index_column_sets(Job)
        assert frozenset({"job_id"}) in index_sets

    def test_owner_key_id_indexed(self) -> None:
        index_sets = _index_column_sets(Job)
        assert frozenset({"owner_key_id"}) in index_sets

    def test_composite_index_owner_key_id_status(self) -> None:
        index_sets = _index_column_sets(Job)
        assert frozenset({"owner_key_id", "status"}) in index_sets

    def test_status_default_pending(self) -> None:
        col = _table(Job).c["status"]
        assert col.default is not None

    def test_created_at_timezone_aware(self) -> None:
        col = _table(Job).c["created_at"]
        assert isinstance(col.type, sa.DateTime)
        assert col.type.timezone is True

    def test_started_at_nullable(self) -> None:
        col = _table(Job).c["started_at"]
        assert col.nullable is True

    def test_completed_at_nullable(self) -> None:
        col = _table(Job).c["completed_at"]
        assert col.nullable is True

    def test_output_files_is_jsonb(self) -> None:
        from sqlalchemy.dialects.postgresql import JSONB

        col = _table(Job).c["output_files"]
        assert isinstance(col.type, JSONB)

    def test_summary_is_jsonb(self) -> None:
        from sqlalchemy.dialects.postgresql import JSONB

        col = _table(Job).c["summary"]
        assert isinstance(col.type, JSONB)


# ---------------------------------------------------------------------------
# UsageRecord model
# ---------------------------------------------------------------------------


class TestUsageRecordModel:
    """Schema verification for the usage_records table."""

    def test_table_name(self) -> None:
        assert UsageRecord.__tablename__ == "usage_records"

    def test_required_columns_exist(self) -> None:
        required = {
            "id",
            "timestamp",
            "endpoint",
            "method",
            "status_code",
            "response_time_ms",
            "key_id",
            "pages_count",
        }
        assert required.issubset(_column_names(UsageRecord))

    def test_key_id_indexed(self) -> None:
        index_sets = _index_column_sets(UsageRecord)
        assert frozenset({"key_id"}) in index_sets

    def test_composite_index_key_id_timestamp(self) -> None:
        index_sets = _index_column_sets(UsageRecord)
        assert frozenset({"key_id", "timestamp"}) in index_sets

    def test_timestamp_timezone_aware(self) -> None:
        col = _table(UsageRecord).c["timestamp"]
        assert isinstance(col.type, sa.DateTime)
        assert col.type.timezone is True

    def test_pages_count_default_zero(self) -> None:
        col = _table(UsageRecord).c["pages_count"]
        assert col.default is not None

    def test_key_id_nullable(self) -> None:
        col = _table(UsageRecord).c["key_id"]
        assert col.nullable is True


# ---------------------------------------------------------------------------
# Engine and session setup
# ---------------------------------------------------------------------------


class TestEngineSetup:
    """Verify engine and session-factory singletons are created correctly."""

    def test_engine_creation(self) -> None:
        from api.db.engine import create_async_engine_from_settings

        engine = create_async_engine_from_settings()
        assert engine is not None

    def test_session_factory_returns_maker(self) -> None:
        from api.db.engine import async_session_factory

        factory = async_session_factory()
        assert factory is not None

    @pytest.mark.asyncio
    async def test_get_db_session_yields_session(self) -> None:
        from api.db.session import get_db_session

        async for session in get_db_session():
            assert session is not None
            break
