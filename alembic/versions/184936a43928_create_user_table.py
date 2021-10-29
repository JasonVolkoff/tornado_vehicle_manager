"""create user table

Revision ID: 184936a43928
Revises: 
Create Date: 2021-10-28 17:21:25.769762

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, BigInteger, String

# revision identifiers, used by Alembic.
revision = '184936a43928'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        Column('id', sa.Integer, primary_key=True),
        Column('username', sa.String(32), nullable=False, unique=True)
    )


def downgrade():
    op.drop_table('users')
