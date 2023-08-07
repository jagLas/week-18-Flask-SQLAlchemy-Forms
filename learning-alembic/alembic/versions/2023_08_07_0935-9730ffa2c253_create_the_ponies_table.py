"""create the ponies table

Revision ID: 9730ffa2c253
Revises: 10e54e8ebcda
Create Date: 2023-08-07 09:35:58.466258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9730ffa2c253'
down_revision: Union[str, None] = '10e54e8ebcda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ponies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("breed", sa.String(20), nullable=False),
        sa.Column("birth_year", sa.Integer, nullable=False),
        sa.Column("owner_id",
                sa.Integer,
                sa.ForeignKey("owners.id"),
                nullable=False)
    )


def downgrade() -> None:
    op.drop_table("ponies")
