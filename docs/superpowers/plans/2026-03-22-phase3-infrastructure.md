# Phase 3: CI/CD + Database + Deployment — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate Parsify from in-memory storage to PostgreSQL, add Docker containerization, GitHub Actions CI, Railway deployment, health endpoints, and structured JSON logging.

**Architecture:** The current API uses 4 in-memory dict-based singletons (JobStore, AuthService, UsageService, BillingService). Phase 3 replaces them with SQLAlchemy 2.0 async models backed by PostgreSQL, adds Alembic for migrations, introduces a repository pattern for data access, and wraps everything in Docker for production. The existing Pydantic schemas and API response contract remain unchanged — only the storage layer is swapped.

**Tech Stack:** Python 3.13, SQLAlchemy 2.0 (async), Alembic, asyncpg, PostgreSQL 16, Docker (multi-stage), docker-compose, GitHub Actions, Railway

**Dependency Graph:**
```
Task 1 (#32 schema) → Task 2 (#33 models+alembic) → Task 3 (#34 migration)
                                                          ↓
Task 7 (#39 health) ──────────────────────────────── Task 4 (#35 Dockerfile) → Task 8 (#38 Railway)
Task 8 (#40 logging) ─────────────────────────────── Task 5 (#36 docker-compose)
                                                      Task 6 (#37 CI)
```

Tasks 6, 7, 8 are independent and can be parallelized after Task 3. Tasks 4+5 depend on Task 3.

---

## File Map

### New Files

| File | Responsibility |
|------|---------------|
| `api/db/__init__.py` | Database package exports |
| `api/db/engine.py` | Async SQLAlchemy engine + session factory |
| `api/db/models.py` | ORM models: User, APIKey, Job, UsageRecord |
| `api/db/session.py` | FastAPI dependency for DB session injection |
| `api/db/repositories.py` | Repository classes with CRUD operations |
| `api/middleware/request_id.py` | Request ID generation + propagation |
| `api/middleware/logging_config.py` | JSON structured logging formatter + setup |
| `alembic.ini` | Alembic config pointing to migrations dir |
| `alembic/env.py` | Alembic async environment with SQLAlchemy models |
| `alembic/script.py.mako` | Alembic migration template |
| `alembic/versions/001_initial_schema.py` | Initial migration (users, api_keys, jobs, usage_records) |
| `Dockerfile` | Multi-stage build: deps → app → runtime |
| `docker-compose.yml` | Local dev: postgres, redis, api, worker |
| `.github/workflows/ci.yml` | Lint + type check + test + build pipeline |
| `railway.json` | Railway deployment config |
| `Procfile` | Process types: web + worker |
| `tests/test_db_models.py` | SQLAlchemy model + repository tests |
| `tests/test_health.py` | Health + readiness endpoint tests |
| `tests/test_logging.py` | Structured logging tests |

### Modified Files

| File | Changes |
|------|---------|
| `api/config.py` | Add `database_url`, `log_level`, `log_format` settings |
| `api/app.py` | DB lifecycle (startup/shutdown), enhanced health/readiness, request ID middleware |
| `api/services/auth_service.py` | Replace in-memory with async repository calls |
| `api/services/job_store.py` | Replace in-memory with async repository calls |
| `api/services/usage.py` | Replace in-memory with async repository calls |
| `api/services/billing.py` | Update user lookups to use async repository |
| `api/middleware/auth.py` | Use async DB lookups for key verification |
| `api/middleware/usage.py` | Use async DB writes for usage recording |
| `api/routers/scrape.py` | Inject DB session dependency |
| `api/routers/jobs.py` | Inject DB session dependency |
| `api/routers/process.py` | Inject DB session dependency |
| `api/routers/auth.py` | Inject DB session dependency |
| `api/routers/billing.py` | Inject DB session dependency |
| `api/routers/usage.py` | Inject DB session dependency |
| `api/workers/scrape_worker.py` | Use DB session for job state |
| `tests/conftest.py` | Add async DB fixtures, test database setup |
| `tests/test_api.py` | Update store resets → DB rollback |
| `tests/test_billing.py` | Update store resets → DB rollback |
| `requirements.txt` | Add sqlalchemy[asyncio], alembic, asyncpg, psycopg2-binary |

---

## Task 1: Design PostgreSQL Schema (#32)

**Files:**
- Create: `api/db/__init__.py`
- Create: `api/db/models.py`
- Modify: `requirements.txt`
- Modify: `api/config.py`
- Test: `tests/test_db_models.py`

This task defines the SQLAlchemy ORM models that map to the PostgreSQL tables. The schema mirrors the existing dataclasses (UserData, APIKeyData, JobData, UsageEntry) with proper indexes and constraints.

- [ ] **Step 1: Add database dependencies to requirements.txt**

Append to `requirements.txt`:
```
# Database (Phase 3)
sqlalchemy[asyncio]>=2.0.0
alembic>=1.13.0
asyncpg>=0.29.0
psycopg2-binary>=2.9.0
```

Run: `pip install -r requirements.txt`

- [ ] **Step 2: Add database_url to Settings**

In `api/config.py`, add to the `Settings` class:
```python
# Database
database_url: str = "postgresql+asyncpg://parsify:parsify@localhost:5432/parsify"
database_echo: bool = False

# Logging
log_level: str = "INFO"
log_format: str = "json"  # "json" or "text"
```

- [ ] **Step 3: Create the db package init**

Create `api/db/__init__.py`:
```python
"""Database package — SQLAlchemy models, engine, and session management."""
```

- [ ] **Step 4: Write failing tests for ORM models**

Create `tests/test_db_models.py`:
```python
"""Tests for SQLAlchemy ORM models (#32)."""

import pytest
from sqlalchemy import inspect

from api.db.models import Base, User, APIKey, Job, UsageRecord


class TestUserModel:
    """Tests for the User ORM model."""

    def test_user_table_name(self) -> None:
        assert User.__tablename__ == "users"

    def test_user_has_required_columns(self) -> None:
        columns = {c.name for c in inspect(User).columns}
        expected = {"id", "user_id", "email", "name", "tier",
                    "stripe_customer_id", "stripe_subscription_id", "created_at"}
        assert expected.issubset(columns)

    def test_user_email_unique_constraint(self) -> None:
        email_col = inspect(User).columns["email"]
        assert email_col.unique is True

    def test_user_id_unique_constraint(self) -> None:
        user_id_col = inspect(User).columns["user_id"]
        assert user_id_col.unique is True


class TestAPIKeyModel:
    """Tests for the APIKey ORM model."""

    def test_api_key_table_name(self) -> None:
        assert APIKey.__tablename__ == "api_keys"

    def test_api_key_has_required_columns(self) -> None:
        columns = {c.name for c in inspect(APIKey).columns}
        expected = {"id", "key_id", "user_id", "name", "prefix",
                    "key_hash", "is_active", "created_at"}
        assert expected.issubset(columns)

    def test_key_hash_indexed(self) -> None:
        key_hash_col = inspect(APIKey).columns["key_hash"]
        assert key_hash_col.index is True or key_hash_col.unique is True


class TestJobModel:
    """Tests for the Job ORM model."""

    def test_job_table_name(self) -> None:
        assert Job.__tablename__ == "jobs"

    def test_job_has_required_columns(self) -> None:
        columns = {c.name for c in inspect(Job).columns}
        expected = {"id", "job_id", "status", "url", "job_type",
                    "max_pages", "output_format", "webhook_url",
                    "created_at", "started_at", "completed_at",
                    "pages_scraped", "pages_failed", "progress",
                    "error_message", "output_files", "summary",
                    "owner_key_id"}
        assert expected.issubset(columns)

    def test_job_id_unique(self) -> None:
        job_id_col = inspect(Job).columns["job_id"]
        assert job_id_col.unique is True


class TestUsageRecordModel:
    """Tests for the UsageRecord ORM model."""

    def test_usage_table_name(self) -> None:
        assert UsageRecord.__tablename__ == "usage_records"

    def test_usage_has_required_columns(self) -> None:
        columns = {c.name for c in inspect(UsageRecord).columns}
        expected = {"id", "timestamp", "endpoint", "method",
                    "status_code", "response_time_ms", "key_id",
                    "pages_count"}
        assert expected.issubset(columns)


class TestBaseMetadata:
    """Tests for the shared Base and metadata."""

    def test_all_tables_registered(self) -> None:
        table_names = set(Base.metadata.tables.keys())
        assert "users" in table_names
        assert "api_keys" in table_names
        assert "jobs" in table_names
        assert "usage_records" in table_names
```

Run: `python -m pytest tests/test_db_models.py -v`
Expected: FAIL (ImportError — models don't exist yet)

- [ ] **Step 5: Implement the SQLAlchemy ORM models**

Create `api/db/models.py`:
```python
"""SQLAlchemy ORM models for Parsify.

Maps to PostgreSQL tables: users, api_keys, jobs, usage_records.
Mirrors existing dataclasses in services/ but with proper DB constraints.
See ADR-002 for design rationale.
"""

from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models."""

    pass


class User(Base):
    """User accounts."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    tier: Mapped[str] = mapped_column(String(20), nullable=False, default="free")
    stripe_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stripe_subscription_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )


class APIKey(Base):
    """API keys for authentication."""

    __tablename__ = "api_keys"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    key_id: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    prefix: Mapped[str] = mapped_column(String(20), nullable=False)
    key_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )


class Job(Base):
    """Scrape and process jobs."""

    __tablename__ = "jobs"
    __table_args__ = (
        Index("ix_jobs_owner_status", "owner_key_id", "status"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    url: Mapped[str] = mapped_column(Text, nullable=False)
    job_type: Mapped[str] = mapped_column(String(20), nullable=False, default="scrape")
    max_pages: Mapped[int] = mapped_column(Integer, nullable=False, default=100)
    output_format: Mapped[str] = mapped_column(String(20), nullable=False, default="markdown")
    webhook_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    pages_scraped: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    pages_failed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    progress: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    output_files: Mapped[dict | None] = mapped_column(JSONB, nullable=True, default=list)
    summary: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    owner_key_id: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)


class UsageRecord(Base):
    """API usage tracking records."""

    __tablename__ = "usage_records"
    __table_args__ = (
        Index("ix_usage_key_timestamp", "key_id", "timestamp"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    endpoint: Mapped[str] = mapped_column(String(255), nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    status_code: Mapped[int] = mapped_column(Integer, nullable=False)
    response_time_ms: Mapped[float] = mapped_column(Float, nullable=False)
    key_id: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    pages_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
```

- [ ] **Step 6: Run tests to verify models pass**

Run: `python -m pytest tests/test_db_models.py -v`
Expected: All PASS

- [ ] **Step 7: Commit**

```bash
git checkout -b feat/issue-32-postgresql-schema
git add api/db/__init__.py api/db/models.py api/config.py requirements.txt tests/test_db_models.py
git commit -m "feat(db): design PostgreSQL schema with SQLAlchemy models - closes #32

Phase: 3
Feature: F003-production-infrastructure

- Define ORM models: User, APIKey, Job, UsageRecord
- Add proper indexes: key_hash, user_id, job_id, owner+status composite
- JSONB columns for output_files and summary
- All timestamps timezone-aware
- Add database_url and logging config to Settings"
```

---

## Task 2: Set Up SQLAlchemy Engine + Alembic Migrations (#33)

**Files:**
- Create: `api/db/engine.py`
- Create: `api/db/session.py`
- Create: `alembic.ini`
- Create: `alembic/env.py`
- Create: `alembic/script.py.mako`
- Create: `alembic/versions/` (auto-generated)
- Test: `tests/test_db_models.py` (extend)

- [ ] **Step 1: Write failing tests for engine and session**

Append to `tests/test_db_models.py`:
```python
import pytest
from unittest.mock import patch

from api.db.engine import create_async_engine_from_settings, async_session_factory
from api.db.session import get_db_session


class TestEngineSetup:
    """Tests for async engine and session factory."""

    def test_engine_creation(self) -> None:
        """Engine is created from settings URL."""
        engine = create_async_engine_from_settings()
        assert engine is not None
        assert "asyncpg" in str(engine.url.drivername) or "sqlite" in str(engine.url.drivername)

    def test_session_factory_returns_maker(self) -> None:
        """Session factory returns an async session maker."""
        factory = async_session_factory()
        assert factory is not None

    @pytest.mark.asyncio
    async def test_get_db_session_yields_session(self) -> None:
        """get_db_session dependency yields a session and closes it."""
        async for session in get_db_session():
            assert session is not None
            break
```

Run: `python -m pytest tests/test_db_models.py::TestEngineSetup -v`
Expected: FAIL (modules don't exist yet)

- [ ] **Step 2: Implement async engine**

Create `api/db/engine.py`:
```python
"""Async SQLAlchemy engine and session factory.

Provides the database connection pool for the entire application.
Uses asyncpg for PostgreSQL, falls back to aiosqlite for testing.
"""

import logging

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from ..config import settings

logger = logging.getLogger(__name__)

_engine: AsyncEngine | None = None
_session_maker: async_sessionmaker[AsyncSession] | None = None


def create_async_engine_from_settings() -> AsyncEngine:
    """Create an async engine from application settings.

    Returns:
        Configured AsyncEngine instance.
    """
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            settings.database_url,
            echo=settings.database_echo,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,
        )
        logger.info("Created async database engine: %s", settings.database_url.split("@")[-1])
    return _engine


def async_session_factory() -> async_sessionmaker[AsyncSession]:
    """Get or create the async session factory.

    Returns:
        Configured async_sessionmaker.
    """
    global _session_maker
    if _session_maker is None:
        engine = create_async_engine_from_settings()
        _session_maker = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_maker


async def dispose_engine() -> None:
    """Dispose of the engine connection pool. Call on shutdown."""
    global _engine, _session_maker
    if _engine is not None:
        await _engine.dispose()
        _engine = None
        _session_maker = None
        logger.info("Database engine disposed")
```

- [ ] **Step 3: Implement session dependency**

Create `api/db/session.py`:
```python
"""FastAPI dependency for database session injection.

Usage in routers:
    from api.db.session import get_db_session

    @router.get("/items")
    async def list_items(db: AsyncSession = Depends(get_db_session)):
        ...
"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from .engine import async_session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async database session, auto-closing on exit.

    Yields:
        AsyncSession bound to the current request.
    """
    factory = async_session_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

- [ ] **Step 4: Run engine/session tests**

Run: `python -m pytest tests/test_db_models.py::TestEngineSetup -v`
Expected: PASS (engine creates, session yields)

- [ ] **Step 5: Initialize Alembic**

Run: `cd /Volumes/NvME-Satechi/1-PROJECTS/Development/PHASE_I/DocScraper && alembic init alembic`

Then replace `alembic/env.py` with the async version:
```python
"""Alembic environment configuration for async SQLAlchemy."""

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from api.config import settings
from api.db.models import Base

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode (SQL generation only)."""
    url = settings.database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    """Execute migrations using the given connection."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations in online async mode."""
    connectable = create_async_engine(settings.database_url, pool_pre_ping=True)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    """Entry point for online migration execution."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

Update `alembic.ini`:
- Set `sqlalchemy.url` to empty (we read from settings)
- Ensure `script_location = alembic`

- [ ] **Step 6: Generate the initial migration**

Run: `alembic revision --autogenerate -m "initial schema: users, api_keys, jobs, usage_records"`

Verify the generated migration file exists in `alembic/versions/`.

- [ ] **Step 7: Commit**

```bash
git add api/db/engine.py api/db/session.py alembic.ini alembic/ tests/test_db_models.py
git commit -m "feat(db): set up SQLAlchemy async engine and Alembic migrations - closes #33

Phase: 3
Feature: F003-production-infrastructure

- Async engine with connection pooling (pool_size=10, overflow=20)
- Session dependency with auto-commit/rollback
- Alembic configured for async migrations
- Initial migration: users, api_keys, jobs, usage_records tables"
```

---

## Task 3: Migrate from In-Memory to PostgreSQL (#34)

**Files:**
- Create: `api/db/repositories.py`
- Modify: `api/services/auth_service.py`
- Modify: `api/services/job_store.py`
- Modify: `api/services/usage.py`
- Modify: `api/services/billing.py`
- Modify: `api/middleware/auth.py`
- Modify: `api/middleware/usage.py`
- Modify: `api/routers/scrape.py`
- Modify: `api/routers/jobs.py`
- Modify: `api/routers/process.py`
- Modify: `api/routers/auth.py`
- Modify: `api/routers/billing.py`
- Modify: `api/routers/usage.py`
- Modify: `api/workers/scrape_worker.py`
- Modify: `api/app.py`
- Modify: `tests/conftest.py`
- Modify: `tests/test_api.py`
- Modify: `tests/test_billing.py`
- Test: `tests/test_db_models.py` (extend with repository tests)

This is the largest task. The strategy: create a repository layer, update services to accept a DB session, update routers to inject the session, then update tests.

- [ ] **Step 1: Write failing tests for repositories**

Append repository tests to `tests/test_db_models.py`:
```python
from api.db.repositories import UserRepository, APIKeyRepository, JobRepository, UsageRepository


class TestUserRepository:
    """Tests for UserRepository CRUD."""

    @pytest.mark.asyncio
    async def test_create_and_get_user(self, db_session) -> None:
        repo = UserRepository(db_session)
        user = await repo.create(email="test@example.com", name="Test")
        assert user.user_id.startswith("user_")

        fetched = await repo.get_by_user_id(user.user_id)
        assert fetched is not None
        assert fetched.email == "test@example.com"

    @pytest.mark.asyncio
    async def test_get_by_email(self, db_session) -> None:
        repo = UserRepository(db_session)
        await repo.create(email="find@example.com")

        found = await repo.get_by_email("find@example.com")
        assert found is not None
        assert found.email == "find@example.com"

    @pytest.mark.asyncio
    async def test_duplicate_email_raises(self, db_session) -> None:
        repo = UserRepository(db_session)
        await repo.create(email="dupe@example.com")
        with pytest.raises(ValueError, match="already registered"):
            await repo.create(email="dupe@example.com")

    @pytest.mark.asyncio
    async def test_update_user(self, db_session) -> None:
        repo = UserRepository(db_session)
        user = await repo.create(email="update@example.com")
        updated = await repo.update(user.user_id, tier="pro", name="Updated")
        assert updated.tier == "pro"
        assert updated.name == "Updated"


class TestAPIKeyRepository:
    """Tests for APIKeyRepository CRUD."""

    @pytest.mark.asyncio
    async def test_create_and_verify_key(self, db_session) -> None:
        user_repo = UserRepository(db_session)
        user = await user_repo.create(email="keys@example.com")

        key_repo = APIKeyRepository(db_session)
        key_data, raw_key = await key_repo.create(user_id=user.user_id, name="Test Key")
        assert raw_key.startswith("pk_")

        verified = await key_repo.verify(raw_key)
        assert verified is not None
        assert verified.key_id == key_data.key_id

    @pytest.mark.asyncio
    async def test_revoke_key(self, db_session) -> None:
        user_repo = UserRepository(db_session)
        user = await user_repo.create(email="revoke@example.com")

        key_repo = APIKeyRepository(db_session)
        key_data, raw_key = await key_repo.create(user_id=user.user_id, name="Revoke Me")

        success = await key_repo.revoke(key_data.key_id, user.user_id)
        assert success is True

        verified = await key_repo.verify(raw_key)
        assert verified is None


class TestJobRepository:
    """Tests for JobRepository CRUD."""

    @pytest.mark.asyncio
    async def test_create_and_get_job(self, db_session) -> None:
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com", job_type="scrape")
        assert job.job_id.startswith("job_")

        fetched = await repo.get(job.job_id)
        assert fetched is not None
        assert fetched.url == "https://docs.example.com"

    @pytest.mark.asyncio
    async def test_update_job_status(self, db_session) -> None:
        repo = JobRepository(db_session)
        job = await repo.create(url="https://docs.example.com")
        updated = await repo.update(job.job_id, status="running")
        assert updated.status == "running"

    @pytest.mark.asyncio
    async def test_list_jobs_with_filter(self, db_session) -> None:
        repo = JobRepository(db_session)
        await repo.create(url="https://a.com")
        await repo.create(url="https://b.com")

        jobs, total = await repo.list_jobs(limit=50, offset=0)
        assert total == 2
        assert len(jobs) == 2
```

Expected: FAIL (repositories don't exist)

- [ ] **Step 2: Create the test database fixture**

Update `tests/conftest.py` to add async DB fixtures:
```python
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.db.models import Base


@pytest_asyncio.fixture
async def db_session():
    """Create a fresh in-memory SQLite database for each test.

    Uses SQLite for test speed — no PostgreSQL needed for unit tests.
    """
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with maker() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()
```

Also add `aiosqlite>=0.20.0` to `requirements.txt` under a test dependencies comment.

- [ ] **Step 3: Implement repositories**

Create `api/db/repositories.py`:
```python
"""Repository classes for database CRUD operations.

Each repository encapsulates SQL queries for one domain entity.
All methods accept an AsyncSession and return ORM model instances.
"""

import hashlib
import logging
import secrets
import uuid
from typing import Optional

from sqlalchemy import func, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import settings
from .models import APIKey, Job, UsageRecord, User

logger = logging.getLogger(__name__)


class UserRepository:
    """CRUD operations for User entities."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(
        self, email: str, name: Optional[str] = None, tier: str = "free",
    ) -> User:
        existing = await self.get_by_email(email)
        if existing is not None:
            raise ValueError(f"Email already registered: {email}")

        user = User(
            user_id=f"user_{uuid.uuid4().hex[:12]}",
            email=email,
            name=name,
            tier=tier,
        )
        self._session.add(user)
        await self._session.flush()
        return user

    async def get_by_user_id(self, user_id: str) -> Optional[User]:
        result = await self._session.execute(
            select(User).where(User.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self._session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def update(self, user_id: str, **kwargs) -> Optional[User]:
        user = await self.get_by_user_id(user_id)
        if user is None:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        await self._session.flush()
        return user

    async def get_by_stripe_customer_id(self, customer_id: str) -> Optional[User]:
        result = await self._session.execute(
            select(User).where(User.stripe_customer_id == customer_id)
        )
        return result.scalar_one_or_none()


class APIKeyRepository:
    """CRUD operations for API Key entities."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @staticmethod
    def _hash_key(raw_key: str) -> str:
        return hashlib.sha256(raw_key.encode()).hexdigest()

    async def create(self, user_id: str, name: str) -> tuple[APIKey, str]:
        raw_key = f"{settings.api_key_prefix}{secrets.token_hex(32)}"
        prefix = raw_key[: len(settings.api_key_prefix) + 8]
        key_hash = self._hash_key(raw_key)

        api_key = APIKey(
            key_id=f"key_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            name=name,
            prefix=prefix,
            key_hash=key_hash,
        )
        self._session.add(api_key)
        await self._session.flush()
        return api_key, raw_key

    async def verify(self, raw_key: str) -> Optional[APIKey]:
        key_hash = self._hash_key(raw_key)
        result = await self._session.execute(
            select(APIKey).where(
                APIKey.key_hash == key_hash,
                APIKey.is_active == True,
            )
        )
        return result.scalar_one_or_none()

    async def revoke(self, key_id: str, user_id: str) -> bool:
        result = await self._session.execute(
            select(APIKey).where(
                APIKey.key_id == key_id,
                APIKey.user_id == user_id,
            )
        )
        key = result.scalar_one_or_none()
        if key is None:
            return False
        key.is_active = False
        await self._session.flush()
        return True

    async def list_for_user(self, user_id: str) -> list[APIKey]:
        result = await self._session.execute(
            select(APIKey).where(APIKey.user_id == user_id)
        )
        return list(result.scalars().all())


class JobRepository:
    """CRUD operations for Job entities."""

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
        job = Job(
            job_id=f"job_{uuid.uuid4().hex[:12]}",
            status="pending",
            url=url,
            job_type=job_type,
            max_pages=max_pages,
            output_format=output_format,
            webhook_url=webhook_url,
            owner_key_id=owner_key_id,
        )
        self._session.add(job)
        await self._session.flush()
        return job

    async def get(self, job_id: str) -> Optional[Job]:
        result = await self._session.execute(
            select(Job).where(Job.job_id == job_id)
        )
        return result.scalar_one_or_none()

    async def update(self, job_id: str, **kwargs) -> Optional[Job]:
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
        query = select(Job)
        count_query = select(func.count()).select_from(Job)

        if owner_key_id is not None:
            query = query.where(Job.owner_key_id == owner_key_id)
            count_query = count_query.where(Job.owner_key_id == owner_key_id)
        if status is not None:
            query = query.where(Job.status == status)
            count_query = count_query.where(Job.status == status)

        query = query.order_by(Job.created_at.desc()).offset(offset).limit(limit)

        result = await self._session.execute(query)
        count_result = await self._session.execute(count_query)

        return list(result.scalars().all()), count_result.scalar_one()

    async def delete(self, job_id: str) -> bool:
        job = await self.get(job_id)
        if job is None:
            return False
        await self._session.delete(job)
        await self._session.flush()
        return True


class UsageRepository:
    """CRUD operations for UsageRecord entities."""

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
        entry = UsageRecord(
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            response_time_ms=response_time_ms,
            key_id=key_id,
            pages_count=pages_count,
        )
        self._session.add(entry)
        await self._session.flush()
        return entry

    async def get_hourly_count(self, key_id: str) -> int:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        hour_start = now.replace(minute=0, second=0, microsecond=0)

        result = await self._session.execute(
            select(func.count()).select_from(UsageRecord).where(
                UsageRecord.key_id == key_id,
                UsageRecord.timestamp >= hour_start,
            )
        )
        return result.scalar_one()

    async def get_daily_breakdown(
        self, key_id: str, days: int = 30,
    ) -> list[dict]:
        from datetime import datetime, timedelta, timezone

        now = datetime.now(timezone.utc)
        results = []

        for i in range(days):
            day_start = (now - timedelta(days=i)).replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            day_end = day_start + timedelta(days=1)

            count_result = await self._session.execute(
                select(
                    func.count(),
                    func.coalesce(func.sum(UsageRecord.pages_count), 0),
                    func.count().filter(UsageRecord.status_code >= 400),
                ).select_from(UsageRecord).where(
                    UsageRecord.key_id == key_id,
                    UsageRecord.timestamp >= day_start,
                    UsageRecord.timestamp < day_end,
                )
            )
            row = count_result.one()
            results.append({
                "date": day_start.strftime("%Y-%m-%d"),
                "request_count": row[0],
                "pages_scraped": row[1],
                "errors": row[2],
            })

        return results
```

- [ ] **Step 4: Run repository tests**

Run: `python -m pytest tests/test_db_models.py -v -k "Repository"`
Expected: All PASS

- [ ] **Step 5: Update app.py with DB lifecycle and version bump**

Update `api/app.py` to add startup/shutdown hooks:
```python
"""Parsify REST API application factory."""

import logging

from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded

from .db.engine import create_async_engine_from_settings, dispose_engine
from .middleware.rate_limit import limiter, rate_limit_exceeded_handler
from .middleware.usage import UsageTrackingMiddleware

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage application lifespan: DB engine startup and shutdown."""
    create_async_engine_from_settings()
    logger.info("Database engine initialized")
    yield
    await dispose_engine()
    logger.info("Database engine disposed")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Parsify API",
        description="Documentation scraping and processing REST API",
        version="0.3.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )

    # --- Middleware ---
    app.add_middleware(UsageTrackingMiddleware)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

    # --- Routers ---
    from .routers import auth, billing, jobs, process, scrape, usage
    app.include_router(scrape.router, prefix="/api/v1")
    app.include_router(jobs.router, prefix="/api/v1")
    app.include_router(process.router, prefix="/api/v1")
    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(billing.router, prefix="/api/v1")
    app.include_router(usage.router, prefix="/api/v1")

    logger.info("Parsify API application created (version 0.3.0)")
    return app


app = create_app()
```

- [ ] **Step 6: Update all routers to inject DB session and use repositories**

Each router gets `db: AsyncSession = Depends(get_db_session)` and instantiates the appropriate repository. Example for `scrape.py`:

```python
"""Scrape router — POST /api/v1/scrape endpoint."""

import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import get_db_session
from ..db.repositories import JobRepository
from ..models.schemas import APIResponse, JobStatus, MetaResponse, ScrapeRequest, ScrapeResponse

router = APIRouter(tags=["scrape"])

@router.post("/scrape", response_model=APIResponse, status_code=202)
async def create_scrape_job(
    request: ScrapeRequest,
    db: AsyncSession = Depends(get_db_session),
) -> APIResponse:
    repo = JobRepository(db)
    job = await repo.create(
        url=str(request.url),
        job_type="scrape",
        max_pages=request.max_pages,
        output_format=request.output_format,
        webhook_url=str(request.webhook_url) if request.webhook_url else None,
    )
    return APIResponse(
        data=ScrapeResponse(
            job_id=job.job_id,
            status=JobStatus.PENDING,
            message="Scrape job submitted successfully",
            created_at=job.created_at,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
```

Apply the same pattern to: `jobs.py`, `process.py`, `auth.py`, `billing.py`, `usage.py`.

- [ ] **Step 7: Update middleware to work with DB sessions**

Update `api/middleware/auth.py` to accept a DB session and perform async key lookup:
```python
async def get_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(_bearer_scheme),
    db: AsyncSession = Depends(get_db_session),
) -> Optional[APIKey]:
    if credentials is None:
        return None
    repo = APIKeyRepository(db)
    return await repo.verify(credentials.credentials)
```

- [ ] **Step 8: Update workers to create their own DB sessions**

Update `api/workers/scrape_worker.py` to use `async_session_factory()`:
```python
async def run_scrape_job(ctx: dict[str, Any], job_id: str) -> dict[str, Any]:
    factory = async_session_factory()
    async with factory() as session:
        repo = JobRepository(session)
        job = await repo.get(job_id)
        # ... rest of implementation using repo ...
        await session.commit()
```

- [ ] **Step 9: Update tests to use db_session fixture**

Replace `_reset_stores` autouse fixture in `tests/test_api.py` and `tests/test_billing.py` with the `db_session` approach. Override the `get_db_session` dependency:

```python
from api.db.session import get_db_session

@pytest.fixture
def app(db_session):
    """Create app with overridden DB session."""
    application = create_app()
    application.dependency_overrides[get_db_session] = lambda: db_session
    return application
```

Note: Since tests now use real SQLite-backed sessions, remove all `._jobs.clear()` and `._users.clear()` calls — the db_session fixture handles isolation.

- [ ] **Step 10: Run the full test suite**

Run: `python -m pytest tests/ -v --tb=short`
Expected: All existing tests pass with DB-backed repositories

- [ ] **Step 11: Commit**

```bash
git add api/db/repositories.py api/app.py api/routers/ api/middleware/ api/services/ api/workers/ tests/
git commit -m "refactor(db): migrate from in-memory storage to PostgreSQL - closes #34

Phase: 3
Feature: F003-production-infrastructure

- Repository pattern: UserRepository, APIKeyRepository, JobRepository, UsageRepository
- All routers inject AsyncSession via FastAPI Depends
- Workers use session factory for background job state
- Auth middleware performs async DB key verification
- Tests use SQLite in-memory for speed (db_session fixture)
- App lifecycle manages engine startup/shutdown"
```

---

## Task 4: Create Dockerfile (#35)

**Files:**
- Create: `Dockerfile`
- Create: `.dockerignore`

- [ ] **Step 1: Create .dockerignore**

Create `.dockerignore`:
```
__pycache__
*.pyc
*.pyo
.git
.github
.env*
.venv
venv
*.egg-info
.torvaldsen
.claude
.serena
docs/
tests/
*.md
!requirements.txt
.DS_Store
```

- [ ] **Step 2: Create multi-stage Dockerfile**

Create `Dockerfile`:
```dockerfile
# ---- Stage 1: Dependencies ----
FROM python:3.13-slim AS deps

WORKDIR /app

# Install system dependencies for Playwright and PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Stage 2: Application ----
FROM python:3.13-slim AS runtime

WORKDIR /app

# Install runtime-only system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from deps stage
COPY --from=deps /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin

# Copy application code
COPY src/ src/
COPY api/ api/
COPY alembic/ alembic/
COPY alembic.ini .
COPY pyproject.toml .

# Install the package
RUN pip install --no-cache-dir -e .

# Non-root user for security
RUN useradd -m -r parsify
USER parsify

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

# Default: run the API server
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 3: Verify Docker builds**

Run: `docker build -t parsify:latest .`
Expected: Build completes without errors

- [ ] **Step 4: Commit**

```bash
git add Dockerfile .dockerignore
git commit -m "infrastructure(infra): create multi-stage Dockerfile - closes #35

Phase: 3
Feature: F003-production-infrastructure

- Two-stage build: deps → runtime (smaller final image)
- Non-root user for security
- Health check via curl to /health
- libpq for PostgreSQL, curl for health checks"
```

---

## Task 5: Create docker-compose.yml (#36)

**Files:**
- Create: `docker-compose.yml`
- Create: `.env.example` (update)

- [ ] **Step 1: Create docker-compose.yml**

```yaml
# Local development stack for Parsify
# Usage: docker compose up -d

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: parsify
      POSTGRES_PASSWORD: parsify
      POSTGRES_DB: parsify
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U parsify"]
      interval: 5s
      timeout: 3s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      PARSIFY_DATABASE_URL: postgresql+asyncpg://parsify:parsify@postgres:5432/parsify
      PARSIFY_REDIS_URL: redis://redis:6379
      PARSIFY_DEBUG: "true"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: >
      sh -c "alembic upgrade head &&
             uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload"

  worker:
    build: .
    environment:
      PARSIFY_DATABASE_URL: postgresql+asyncpg://parsify:parsify@postgres:5432/parsify
      PARSIFY_REDIS_URL: redis://redis:6379
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: arq api.workers.scrape_worker.WorkerSettings

volumes:
  pgdata:
```

- [ ] **Step 2: Update .env.example**

Add to `.env.example` (or create if it doesn't exist):
```bash
# Parsify Configuration
PARSIFY_DATABASE_URL=postgresql+asyncpg://parsify:parsify@localhost:5432/parsify
PARSIFY_REDIS_URL=redis://localhost:6379
PARSIFY_DEBUG=true
PARSIFY_LOG_LEVEL=INFO
PARSIFY_LOG_FORMAT=text

# Stripe (optional for Phase 2+)
PARSIFY_STRIPE_SECRET_KEY=
PARSIFY_STRIPE_WEBHOOK_SECRET=
PARSIFY_STRIPE_PRICE_PRO=
PARSIFY_STRIPE_PRICE_ENTERPRISE=

# OpenAI (for classification)
OPENAI_API_KEY=
```

- [ ] **Step 3: Verify compose starts**

Run: `docker compose up -d && docker compose ps`
Expected: All 4 services running healthy

Run: `curl http://localhost:8000/health`
Expected: `{"status": "healthy", "version": "0.3.0"}`

Run: `docker compose down`

- [ ] **Step 4: Commit**

```bash
git add docker-compose.yml .env.example
git commit -m "infrastructure(infra): create docker-compose for local development - closes #36

Phase: 3
Feature: F003-production-infrastructure

- PostgreSQL 16, Redis 7, API, Worker services
- Health check dependencies ensure correct startup order
- API runs migrations on startup then starts uvicorn
- Volume persistence for PostgreSQL data"
```

---

## Task 6: Set Up GitHub Actions CI (#37)

**Files:**
- Create: `.github/workflows/ci.yml`

- [ ] **Step 1: Create CI workflow**

Create `.github/workflows/ci.yml`:
```yaml
name: CI

on:
  push:
    branches: [main, development]
  pull_request:
    branches: [main, development]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: pip
      - run: pip install ruff
      - run: ruff check .

  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: pip
      - run: pip install -r requirements.txt mypy
      - run: mypy api/ --ignore-missing-imports

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: parsify
          POSTGRES_PASSWORD: parsify
          POSTGRES_DB: parsify_test
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U parsify"
          --health-interval 5s
          --health-timeout 3s
          --health-retries 5
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 5s
          --health-timeout 3s
          --health-retries 5
    env:
      PARSIFY_DATABASE_URL: postgresql+asyncpg://parsify:parsify@localhost:5432/parsify_test
      PARSIFY_REDIS_URL: redis://localhost:6379
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: pip
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: pip install -e .
      - run: alembic upgrade head
      - run: python -m pytest tests/ -v --tb=short

  docker:
    runs-on: ubuntu-latest
    needs: [lint, typecheck, test]
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t parsify:ci .
```

- [ ] **Step 2: Commit**

```bash
mkdir -p .github/workflows
git add .github/workflows/ci.yml
git commit -m "infrastructure(infra): set up GitHub Actions CI pipeline - closes #37

Phase: 3
Feature: F003-production-infrastructure

- 4 jobs: lint (ruff), typecheck (mypy), test (pytest + postgres + redis), docker build
- PostgreSQL and Redis service containers for integration tests
- Docker build verifies container builds successfully
- Runs on push to main/development and all PRs"
```

---

## Task 7: Add Health Check and Readiness Endpoints (#39)

**Files:**
- Modify: `api/app.py`
- Test: `tests/test_health.py`

- [ ] **Step 1: Write failing tests for enhanced health endpoints**

Create `tests/test_health.py`:
```python
"""Tests for health and readiness endpoints (#39)."""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from api.app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest_asyncio.fixture
async def client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestHealthEndpoint:
    """Tests for GET /health."""

    @pytest.mark.asyncio
    async def test_health_returns_200(self, client: AsyncClient) -> None:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data
        assert "uptime_seconds" in data

    @pytest.mark.asyncio
    async def test_health_includes_checks(self, client: AsyncClient) -> None:
        response = await client.get("/health")
        data = response.json()
        assert "checks" in data
        assert "database" in data["checks"]
        assert "redis" in data["checks"]


class TestReadinessEndpoint:
    """Tests for GET /ready."""

    @pytest.mark.asyncio
    async def test_readiness_returns_200_when_ready(self, client: AsyncClient) -> None:
        response = await client.get("/ready")
        assert response.status_code in (200, 503)
        data = response.json()
        assert "ready" in data
```

Run: `python -m pytest tests/test_health.py -v`
Expected: FAIL (endpoints don't have enhanced responses)

- [ ] **Step 2: Implement enhanced health and readiness endpoints**

Update the health/readiness routes in `api/app.py`:
```python
import time

_startup_time = time.monotonic()

@app.get("/health")
async def health_check() -> dict:
    """Liveness check with dependency status."""
    db_ok = await _check_database()
    redis_ok = await _check_redis()
    return {
        "status": "healthy",
        "version": "0.3.0",
        "uptime_seconds": round(time.monotonic() - _startup_time, 1),
        "checks": {
            "database": "ok" if db_ok else "error",
            "redis": "ok" if redis_ok else "error",
        },
    }

@app.get("/ready")
async def readiness_check() -> dict:
    """Readiness check — returns 503 if dependencies are down."""
    from fastapi.responses import JSONResponse
    db_ok = await _check_database()
    redis_ok = await _check_redis()
    ready = db_ok and redis_ok
    content = {"ready": ready, "database": db_ok, "redis": redis_ok}
    if not ready:
        return JSONResponse(content=content, status_code=503)
    return content
```

Add helper functions:
```python
async def _check_database() -> bool:
    try:
        from .db.engine import async_session_factory
        factory = async_session_factory()
        async with factory() as session:
            await session.execute(text("SELECT 1"))
        return True
    except Exception:
        return False

async def _check_redis() -> bool:
    try:
        import redis.asyncio as aioredis
        from .config import settings
        r = aioredis.from_url(settings.redis_url)
        await r.ping()
        await r.aclose()
        return True
    except Exception:
        return False
```

- [ ] **Step 3: Run tests**

Run: `python -m pytest tests/test_health.py -v`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add api/app.py tests/test_health.py
git commit -m "feat(api): add health check and readiness endpoints - closes #39

Phase: 3
Feature: F003-production-infrastructure

- GET /health: liveness check with DB + Redis status, uptime
- GET /ready: readiness check, returns 503 if dependencies down
- Both endpoints check PostgreSQL and Redis connectivity"
```

---

## Task 8: Set Up Structured JSON Logging (#40)

**Files:**
- Create: `api/middleware/logging_config.py`
- Create: `api/middleware/request_id.py`
- Modify: `api/app.py`
- Test: `tests/test_logging.py`

- [ ] **Step 1: Write failing tests for structured logging**

Create `tests/test_logging.py`:
```python
"""Tests for structured JSON logging and request tracing (#40)."""

import json
import logging
import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from api.middleware.logging_config import JSONFormatter, setup_logging
from api.middleware.request_id import REQUEST_ID_HEADER


class TestJSONFormatter:
    """Tests for the JSON log formatter."""

    def test_format_produces_valid_json(self) -> None:
        formatter = JSONFormatter()
        record = logging.LogRecord(
            name="test", level=logging.INFO, pathname="test.py",
            lineno=1, msg="test message", args=(), exc_info=None,
        )
        output = formatter.format(record)
        parsed = json.loads(output)
        assert parsed["message"] == "test message"
        assert parsed["level"] == "INFO"
        assert "timestamp" in parsed

    def test_format_includes_extra_fields(self) -> None:
        formatter = JSONFormatter()
        record = logging.LogRecord(
            name="test", level=logging.INFO, pathname="test.py",
            lineno=1, msg="test", args=(), exc_info=None,
        )
        record.request_id = "req_abc123"
        output = formatter.format(record)
        parsed = json.loads(output)
        assert parsed["request_id"] == "req_abc123"


class TestRequestIDMiddleware:
    """Tests for request ID tracing."""

    @pytest.fixture
    def app(self):
        from api.app import create_app
        return create_app()

    @pytest_asyncio.fixture
    async def client(self, app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

    @pytest.mark.asyncio
    async def test_response_has_request_id_header(self, client: AsyncClient) -> None:
        response = await client.get("/health")
        assert REQUEST_ID_HEADER in response.headers

    @pytest.mark.asyncio
    async def test_client_request_id_preserved(self, client: AsyncClient) -> None:
        response = await client.get(
            "/health",
            headers={REQUEST_ID_HEADER: "custom-id-123"},
        )
        assert response.headers[REQUEST_ID_HEADER] == "custom-id-123"
```

Run: `python -m pytest tests/test_logging.py -v`
Expected: FAIL

- [ ] **Step 2: Implement JSON formatter**

Create `api/middleware/logging_config.py`:
```python
"""Structured JSON logging configuration (#40).

Provides a JSON formatter for production use and a text formatter
for development. Configurable via PARSIFY_LOG_FORMAT setting.
"""

import json
import logging
import sys
from datetime import datetime, timezone

from ..config import settings


class JSONFormatter(logging.Formatter):
    """Format log records as single-line JSON objects."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Include request_id if present
        if hasattr(record, "request_id"):
            log_entry["request_id"] = record.request_id

        # Include exception info
        if record.exc_info and record.exc_info[1]:
            log_entry["exception"] = self.formatException(record.exc_info)

        # Include any extra fields
        for key in ("method", "path", "status_code", "duration_ms"):
            if hasattr(record, key):
                log_entry[key] = getattr(record, key)

        return json.dumps(log_entry, default=str)


def setup_logging() -> None:
    """Configure application logging based on settings."""
    root = logging.getLogger()
    root.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

    # Remove existing handlers
    root.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)

    if settings.log_format == "json":
        handler.setFormatter(JSONFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)-8s %(name)s — %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

    root.addHandler(handler)

    # Quiet noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.INFO if settings.database_echo else logging.WARNING
    )
```

- [ ] **Step 3: Implement request ID middleware**

Create `api/middleware/request_id.py`:
```python
"""Request ID tracing middleware (#40).

Generates a unique request ID for each request and propagates it
through response headers and log records.
"""

import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Attach a unique request ID to every request/response cycle."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Use client-provided ID or generate one
        request_id = request.headers.get(REQUEST_ID_HEADER, f"req_{uuid.uuid4().hex[:12]}")
        request.state.request_id = request_id

        response = await call_next(request)
        response.headers[REQUEST_ID_HEADER] = request_id

        return response
```

- [ ] **Step 4: Wire middleware and logging into app.py**

Add to `create_app()` in `api/app.py`:
```python
from .middleware.request_id import RequestIDMiddleware
from .middleware.logging_config import setup_logging

# At the top of create_app():
setup_logging()

# Add middleware (after usage tracking):
app.add_middleware(RequestIDMiddleware)
```

- [ ] **Step 5: Run tests**

Run: `python -m pytest tests/test_logging.py -v`
Expected: All PASS

- [ ] **Step 6: Commit**

```bash
git add api/middleware/logging_config.py api/middleware/request_id.py api/app.py tests/test_logging.py
git commit -m "feat(core): set up structured JSON logging with request tracing - closes #40

Phase: 3
Feature: F003-production-infrastructure

- JSONFormatter: single-line JSON log records with timestamp, level, message
- RequestIDMiddleware: generates X-Request-ID, preserves client-provided IDs
- Configurable format: 'json' for production, 'text' for development
- Quiet noisy loggers (uvicorn.access, sqlalchemy.engine)"
```

---

## Task 9: Configure Railway Deployment (#38)

**Files:**
- Create: `railway.json`
- Create: `Procfile`

- [ ] **Step 1: Create Procfile**

Create `Procfile`:
```
web: alembic upgrade head && uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}
worker: arq api.workers.scrape_worker.WorkerSettings
```

- [ ] **Step 2: Create railway.json**

Create `railway.json`:
```json
{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "startCommand": "alembic upgrade head && uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}",
    "healthcheckPath": "/health",
    "healthcheckTimeout": 30,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 3
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add railway.json Procfile
git commit -m "infrastructure(infra): configure Railway production deployment - closes #38

Phase: 3
Feature: F003-production-infrastructure

- Procfile: web (API + migrations) and worker processes
- railway.json: Dockerfile builder, health check, restart policy
- Migrations run before API starts to ensure schema is current"
```

---

## Final Verification

After all 9 tasks are complete:

- [ ] **Run the full test suite**

```bash
python -m pytest tests/ -v --tb=short
```

- [ ] **Run linting and type checks**

```bash
ruff check . && mypy api/ --ignore-missing-imports
```

- [ ] **Verify Docker build**

```bash
docker build -t parsify:phase3 .
```

- [ ] **Verify docker-compose**

```bash
docker compose up -d
curl http://localhost:8000/health
curl http://localhost:8000/ready
docker compose down
```

- [ ] **Update PROJECT-STATUS.md** (separate docs commit)

```bash
git commit -m "docs(status): update project status after Phase 3 completion"
```

- [ ] **Run /phase-gate 3** to verify phase completion
