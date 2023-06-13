"""add last few columns to posts table

Revision ID: 53caba6602b5
Revises: e9a9395ec8ea
Create Date: 2023-06-11 19:42:13.743208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53caba6602b5'
down_revision = 'e9a9395ec8ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
