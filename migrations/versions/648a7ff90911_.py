"""empty message

Revision ID: 648a7ff90911
Revises: ee8f4c899a47
Create Date: 2024-12-08 05:08:33.003094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '648a7ff90911'
down_revision = 'ee8f4c899a47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planet', ['planet_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planet_id')

    # ### end Alembic commands ###