"""domicile column

Revision ID: 18b78aff471a
Revises: fc40a04ac397
Create Date: 2020-05-27 13:06:39.671059

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '18b78aff471a'
down_revision = 'fc40a04ac397'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('domicile', sa.Text(), nullable=False))
    op.add_column('persons_history', sa.Column('person', postgresql.UUID(as_uuid=True), nullable=True))
    op.drop_constraint('persons_history_person_id_fkey', 'persons_history', type_='foreignkey')
    op.create_foreign_key(None, 'persons_history', 'persons', ['person'], ['id'])
    op.drop_column('persons_history', 'person_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons_history', sa.Column('person_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'persons_history', type_='foreignkey')
    op.create_foreign_key('persons_history_person_id_fkey', 'persons_history', 'persons', ['person_id'], ['id'])
    op.drop_column('persons_history', 'person')
    op.drop_column('persons', 'domicile')
    # ### end Alembic commands ###
