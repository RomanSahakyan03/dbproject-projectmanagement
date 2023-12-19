"""Add_json_data_to_projects

Revision ID: d385f6f8422e
Revises: 
Create Date: 2023-12-19 21:25:48.424127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd385f6f8422e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('projects', sa.Column('json_data', sa.JSON))

def downgrade():
    op.drop_column('projects', 'json_data')
