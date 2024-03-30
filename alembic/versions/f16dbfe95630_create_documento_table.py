"""create documento table

Revision ID: f16dbfe95630
Revises: 31224d1e3790
Create Date: 2024-03-30 10:51:51.378263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f16dbfe95630'
down_revision: Union[str, None] = '31224d1e3790'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'documento',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tipo', sa.String(3), nullable=False),
        sa.Column('data_emissione', sa.Date),
        sa.Column('numeratore', sa.String(2), nullable=True),
        sa.Column('numero', sa.Integer),
        sa.Column('cliente_id', sa.Integer, nullable=True),
        sa.Column('codice_fiscale', sa.String(16), nullable=False),
        sa.Column('riferimento', sa.String(255), nullable=True),
        sa.Column('descrizione', sa.Text, nullable=True),
        sa.Column('importo', sa.Integer, default=0),
    )


def downgrade() -> None:
    op.drop_table('documento')
