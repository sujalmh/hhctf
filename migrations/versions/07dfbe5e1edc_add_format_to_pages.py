"""Add format to Pages

Revision ID: 07dfbe5e1edc
Revises: 75e8ab9a0014
Create Date: 2021-06-15 19:57:37.410152

"""
from alembic import op  # noqa: I001
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "07dfbe5e1edc"
down_revision = "75e8ab9a0014"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("pages", sa.Column("format", sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("pages", "format")
    # ### end Alembic commands ###
