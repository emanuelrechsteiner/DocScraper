"""add clerk_user_id to users

Revision ID: 31d1c2251f30
Revises: 69c02554
Create Date: 2026-03-23 08:57:20.923384

"""
from __future__ import annotations

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31d1c2251f30'
down_revision: Union[str, None] = '69c02554'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('clerk_user_id', sa.String(64), nullable=True))
    op.create_unique_constraint('uq_users_clerk_user_id', 'users', ['clerk_user_id'])
    op.create_index('ix_users_clerk_user_id', 'users', ['clerk_user_id'])


def downgrade() -> None:
    op.drop_index('ix_users_clerk_user_id', table_name='users')
    op.drop_constraint('uq_users_clerk_user_id', 'users', type_='unique')
    op.drop_column('users', 'clerk_user_id')
