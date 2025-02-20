"""empty message

Revision ID: 2ed067395ded
Revises: 46a278193a94
Create Date: 2023-05-22 13:26:14.692632

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2ed067395ded'
down_revision = '46a278193a94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='teams')
    op.create_unique_constraint(None, 'teams', ['name'])
    op.drop_column('teams', 'email')
    op.drop_column('teams', 'country')
    op.drop_column('teams', 'website')
    op.drop_column('teams', 'bracket')
    op.drop_column('teams', 'affiliation')
    op.add_column('users', sa.Column('as_member', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('service', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('site', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('surname', sa.String(length=128), nullable=True))
    op.drop_column('users', 'website')
    op.drop_column('users', 'bracket')
    op.drop_column('users', 'affiliation')
    op.drop_column('users', 'country')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('country', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=True))
    op.add_column('users', sa.Column('affiliation', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.add_column('users', sa.Column('bracket', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=True))
    op.add_column('users', sa.Column('website', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.drop_column('users', 'surname')
    op.drop_column('users', 'site')
    op.drop_column('users', 'service')
    op.drop_column('users', 'as_member')
    op.add_column('teams', sa.Column('affiliation', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.add_column('teams', sa.Column('bracket', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=True))
    op.add_column('teams', sa.Column('website', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.add_column('teams', sa.Column('country', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=True))
    op.add_column('teams', sa.Column('email', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.drop_constraint(None, 'teams', type_='unique')
    op.create_index('email', 'teams', ['email'], unique=True)
    # ### end Alembic commands ###
