"""Alert Types

Revision ID: e69aca08d73f
Revises: e914d20f5ac0
Create Date: 2022-04-03 13:57:54.004481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e69aca08d73f'
down_revision = 'e914d20f5ac0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alert_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alert_types_id'), 'alert_types', ['id'], unique=False)
    op.create_index(op.f('ix_alert_types_name'), 'alert_types', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_alert_types_name'), table_name='alert_types')
    op.drop_index(op.f('ix_alert_types_id'), table_name='alert_types')
    op.drop_table('alert_types')
    # ### end Alembic commands ###
