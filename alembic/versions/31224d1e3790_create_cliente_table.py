"""create cliente table

Revision ID: 31224d1e3790
Revises: 843119860a99
Create Date: 2024-03-30 10:51:46.307026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31224d1e3790'
down_revision: Union[str, None] = '843119860a99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'cliente',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cognome', sa.String(64), nullable=False),
        sa.Column('nome', sa.String(64), nullable=False),
        sa.Column('email', sa.String(128), nullable=False),
        sa.Column('cellulare', sa.String(64), nullable=True),
        sa.Column('luogo_nascita', sa.String(64), nullable=True),
        sa.Column('provincia_nascita', sa.String(2), nullable=True),
        sa.Column('data_nascita', sa.Date, nullable=True),
        sa.Column('codice_fiscale', sa.String(16), nullable=True),
        sa.Column('residenza_indirizzo', sa.String(128), nullable=True),
        sa.Column('residenza_comune', sa.String(128), nullable=True),
        sa.Column('residenza_provincia', sa.String(2), nullable=True),
        sa.Column('residenza_cap', sa.String(5), nullable=True),
        sa.Column('note', sa.Text, nullable=True),
        sa.Column('data_creazione', sa.DateTime, server_default=sa.func.current_timestamp())
    )


def downgrade() -> None:
    op.drop_table('cliente')
