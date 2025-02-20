"""Initial migration.

Revision ID: d85a395afa09
Revises: 2ed067395ded
Create Date: 2023-07-02 21:22:33.658738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85a395afa09'
down_revision = '2ed067395ded'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('cellphone', sa.String(length=16), nullable=True))
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('gender', sa.String(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    op.drop_column('users', 'confirmed')
    op.drop_column('users', 'cellphone')
    # ### end Alembic commands ###
