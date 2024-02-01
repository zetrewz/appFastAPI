"""3 migration

Revision ID: c22e43093410
Revises: 7efc282c8b43
Create Date: 2024-01-30 12:58:34.621787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c22e43093410'
down_revision: Union[str, None] = '7efc282c8b43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_type', sa.String(), nullable=False))
    op.drop_column('users', 'is_worker')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_worker', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('users', 'user_type')
    # ### end Alembic commands ###
