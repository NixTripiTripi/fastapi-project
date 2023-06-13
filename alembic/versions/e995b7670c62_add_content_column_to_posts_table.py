"""add content column to posts table

Revision ID: e995b7670c62
Revises: c47045f87a7a
Create Date: 2023-06-11 17:37:53.281721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e995b7670c62'
down_revision = 'c47045f87a7a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
