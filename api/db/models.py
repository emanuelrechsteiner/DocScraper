"""SQLAlchemy 2.0 ORM models for the Parsify database schema.

Defines the four core tables: users, api_keys, jobs, usage_records.
All timestamps are timezone-aware. JSON columns use PostgreSQL JSONB.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Optional

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

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    """Declarative base for all ORM models."""


class User(Base):
    """Registered Parsify user.

    Attributes:
        id: Auto-incrementing surrogate primary key.
        user_id: Public stable identifier (UUID string).
        email: User's email address — unique.
        clerk_user_id: Clerk authentication user ID — unique when set.
        name: Optional display name.
        tier: Billing tier — "free", "pro", or "enterprise".
        stripe_customer_id: Stripe customer identifier.
        stripe_subscription_id: Active Stripe subscription identifier.
        created_at: UTC timestamp when the record was inserted.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    clerk_user_id: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True, unique=True
    )
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    tier: Mapped[str] = mapped_column(String(32), nullable=False, default="free")
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True
    )
    stripe_subscription_id: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    __table_args__ = (
        Index("ix_users_user_id", "user_id"),
        Index("ix_users_email", "email"),
        Index("ix_users_clerk_user_id", "clerk_user_id"),
    )

    def __repr__(self) -> str:
        return f"<User user_id={self.user_id!r} email={self.email!r} tier={self.tier!r}>"


class APIKey(Base):
    """Hashed API key associated with a user.

    Attributes:
        id: Auto-incrementing surrogate primary key.
        key_id: Public stable identifier for the key.
        user_id: Foreign-key reference to users.user_id.
        name: Human-readable label for the key.
        prefix: Visible prefix shown in listings (e.g. "pk_xxxxxxxx").
        key_hash: bcrypt/SHA-256 hash of the full key — never the raw value.
        is_active: Whether the key can authenticate requests.
        created_at: UTC timestamp when the record was inserted.
    """

    __tablename__ = "api_keys"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    key_id: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    user_id: Mapped[str] = mapped_column(String(64), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    prefix: Mapped[str] = mapped_column(String(32), nullable=False)
    key_hash: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    __table_args__ = (
        Index("ix_api_keys_key_id", "key_id"),
        Index("ix_api_keys_user_id", "user_id"),
        Index("ix_api_keys_key_hash", "key_hash"),
    )

    def __repr__(self) -> str:
        return f"<APIKey key_id={self.key_id!r} name={self.name!r} active={self.is_active!r}>"


class Job(Base):
    """Scrape or process job submitted through the API.

    Attributes:
        id: Auto-incrementing surrogate primary key.
        job_id: Public stable identifier (UUID string).
        status: Current state — "pending", "running", "completed", "failed", "cancelled".
        url: Target URL for scrape jobs.
        job_type: "scrape" or "process".
        max_pages: Page limit configured at submission time.
        output_format: Requested output format.
        webhook_url: Optional callback URL for completion events.
        created_at: UTC timestamp when the job was submitted.
        started_at: UTC timestamp when execution began.
        completed_at: UTC timestamp when execution finished.
        pages_scraped: Count of successfully scraped pages.
        pages_failed: Count of pages that encountered errors.
        progress: Completion percentage (0.0–100.0).
        error_message: Human-readable error if the job failed.
        output_files: JSONB list of output file paths/URLs.
        summary: JSONB arbitrary result metadata.
        owner_key_id: API key that submitted the job.
    """

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="pending")
    url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    job_type: Mapped[str] = mapped_column(String(32), nullable=False)
    max_pages: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    output_format: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    webhook_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    started_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    pages_scraped: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    pages_failed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    progress: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    output_files: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    summary: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    owner_key_id: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    __table_args__ = (
        Index("ix_jobs_job_id", "job_id"),
        Index("ix_jobs_owner_key_id", "owner_key_id"),
        Index("ix_jobs_owner_key_id_status", "owner_key_id", "status"),
    )

    def __repr__(self) -> str:
        return (
            f"<Job job_id={self.job_id!r} status={self.status!r} type={self.job_type!r}>"
        )


class UsageRecord(Base):
    """Single API usage event for billing and analytics.

    Attributes:
        id: Auto-incrementing surrogate primary key.
        timestamp: UTC time when the request was received.
        endpoint: API path that was called.
        method: HTTP method (GET, POST, etc.).
        status_code: HTTP response status code.
        response_time_ms: Request processing time in milliseconds.
        key_id: API key that made the request.
        pages_count: Pages consumed by this request (0 for non-scrape calls).
    """

    __tablename__ = "usage_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    endpoint: Mapped[str] = mapped_column(String(255), nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    status_code: Mapped[int] = mapped_column(Integer, nullable=False)
    response_time_ms: Mapped[float] = mapped_column(Float, nullable=False)
    key_id: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    pages_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    __table_args__ = (
        Index("ix_usage_records_key_id", "key_id"),
        Index("ix_usage_records_key_id_timestamp", "key_id", "timestamp"),
    )

    def __repr__(self) -> str:
        return (
            f"<UsageRecord key_id={self.key_id!r} endpoint={self.endpoint!r} "
            f"status={self.status_code!r}>"
        )
