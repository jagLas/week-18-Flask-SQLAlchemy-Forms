"""add express shipping field to packages table

Revision ID: ec35f8167665
Revises: 7513fa2b04fd
Create Date: 2023-08-07 18:21:37.437924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec35f8167665'
down_revision = '7513fa2b04fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('express', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.drop_column('express')

    # ### end Alembic commands ###
