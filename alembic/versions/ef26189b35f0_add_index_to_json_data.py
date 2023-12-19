"""Add_index_to_json_data

Revision ID: ef26189b35f0
Revises: d385f6f8422e
Create Date: 2023-12-19 21:26:13.016904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ef26189b35f0'
down_revision: Union[str, None] = 'd385f6f8422e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute('CREATE INDEX project_json_data_trgm_gin_idx ON projects USING gin(json_data)')

def downgrade():
    op.drop_index('project_json_data_trgm_gin_idx', 'projects')

