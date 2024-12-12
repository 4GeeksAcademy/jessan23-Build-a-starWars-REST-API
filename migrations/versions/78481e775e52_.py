"""empty message

Revision ID: 78481e775e52
Revises: 
Create Date: 2024-12-12 03:02:17.196606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78481e775e52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('skin_color', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created', sa.String(length=80), nullable=False),
    sa.Column('diameter', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=120), nullable=False),
    sa.Column('consumables', sa.String(length=80), nullable=False),
    sa.Column('created', sa.String(length=80), nullable=False),
    sa.Column('model', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    op.drop_table('vehicle')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
