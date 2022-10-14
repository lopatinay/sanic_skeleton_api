"""init

Revision ID: 91a7687786c0
Revises: 
Create Date: 2022-02-03 15:17:41.594993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91a7687786c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "dummy_model",
        sa.Column("id", sa.Integer, primary_key=True),
    )


def downgrade():
    op.drop_table("dummy_model")
