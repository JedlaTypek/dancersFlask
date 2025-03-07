"""cleaned_unused_models

Revision ID: 20250107_cleaned_unused_models
Revises: 20250107_added_tanecnici
Create Date: 2025-01-07 20:28:12.735553+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20250107_cleaned_unused_models'
down_revision = '20250107_added_tanecnici'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pocet_deti')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pocet_deti',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('jmeno', sa.VARCHAR(length=50), nullable=False),
    sa.Column('pocet_deti', sa.INTEGER(), nullable=False),
    sa.Column('time', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
