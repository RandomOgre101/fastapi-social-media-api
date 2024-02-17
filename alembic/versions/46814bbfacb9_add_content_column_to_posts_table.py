"""add content column to posts table

Revision ID: 46814bbfacb9
Revises: 98a44f7d5d15
Create Date: 2024-02-16 09:46:18.103482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46814bbfacb9'
down_revision: Union[str, None] = '98a44f7d5d15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False)
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
