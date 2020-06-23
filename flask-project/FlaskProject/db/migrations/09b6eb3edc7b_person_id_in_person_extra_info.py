"""person_id in person_extra_info

Revision ID: 09b6eb3edc7b
Revises: 36de5edd0f5c
Create Date: 2020-06-22 13:53:50.584686

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '09b6eb3edc7b'
down_revision = '36de5edd0f5c'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person_extra_info', 'person_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person_extra_info', 'person_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###
