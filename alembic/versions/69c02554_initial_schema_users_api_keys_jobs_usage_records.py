"""initial schema: users, api_keys, jobs, usage_records

Revision ID: 69c02554
Revises:
Create Date: 2026-03-22 00:00:00.000000

"""
from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "69c02554"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # --- users -----------------------------------------------------------
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.String(length=64), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("tier", sa.String(length=32), nullable=False),
        sa.Column("stripe_customer_id", sa.String(length=64), nullable=True),
        sa.Column("stripe_subscription_id", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index("ix_users_email", "users", ["email"])
    op.create_index("ix_users_user_id", "users", ["user_id"])

    # --- api_keys --------------------------------------------------------
    op.create_table(
        "api_keys",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("key_id", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("prefix", sa.String(length=32), nullable=False),
        sa.Column("key_hash", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key_hash"),
        sa.UniqueConstraint("key_id"),
    )
    op.create_index("ix_api_keys_key_hash", "api_keys", ["key_hash"])
    op.create_index("ix_api_keys_key_id", "api_keys", ["key_id"])
    op.create_index("ix_api_keys_user_id", "api_keys", ["user_id"])

    # --- jobs ------------------------------------------------------------
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("job_id", sa.String(length=64), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("url", sa.Text(), nullable=True),
        sa.Column("job_type", sa.String(length=32), nullable=False),
        sa.Column("max_pages", sa.Integer(), nullable=True),
        sa.Column("output_format", sa.String(length=32), nullable=True),
        sa.Column("webhook_url", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("pages_scraped", sa.Integer(), nullable=False),
        sa.Column("pages_failed", sa.Integer(), nullable=False),
        sa.Column("progress", sa.Float(), nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("output_files", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("summary", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("owner_key_id", sa.String(length=64), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("job_id"),
    )
    op.create_index("ix_jobs_job_id", "jobs", ["job_id"])
    op.create_index("ix_jobs_owner_key_id", "jobs", ["owner_key_id"])
    op.create_index("ix_jobs_owner_key_id_status", "jobs", ["owner_key_id", "status"])

    # --- usage_records ---------------------------------------------------
    op.create_table(
        "usage_records",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("endpoint", sa.String(length=255), nullable=False),
        sa.Column("method", sa.String(length=10), nullable=False),
        sa.Column("status_code", sa.Integer(), nullable=False),
        sa.Column("response_time_ms", sa.Float(), nullable=False),
        sa.Column("key_id", sa.String(length=64), nullable=True),
        sa.Column("pages_count", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_usage_records_key_id", "usage_records", ["key_id"])
    op.create_index(
        "ix_usage_records_key_id_timestamp", "usage_records", ["key_id", "timestamp"]
    )


def downgrade() -> None:
    op.drop_index("ix_usage_records_key_id_timestamp", table_name="usage_records")
    op.drop_index("ix_usage_records_key_id", table_name="usage_records")
    op.drop_table("usage_records")

    op.drop_index("ix_jobs_owner_key_id_status", table_name="jobs")
    op.drop_index("ix_jobs_owner_key_id", table_name="jobs")
    op.drop_index("ix_jobs_job_id", table_name="jobs")
    op.drop_table("jobs")

    op.drop_index("ix_api_keys_user_id", table_name="api_keys")
    op.drop_index("ix_api_keys_key_id", table_name="api_keys")
    op.drop_index("ix_api_keys_key_hash", table_name="api_keys")
    op.drop_table("api_keys")

    op.drop_index("ix_users_user_id", table_name="users")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
