"""create utente table

Revision ID: 843119860a99
Revises: 
Create Date: 2024-03-30 10:38:24.544075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '843119860a99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'utente',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(128), nullable=False),
        sa.Column('password', sa.String(128), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('utente')
