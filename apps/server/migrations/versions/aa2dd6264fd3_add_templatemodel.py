"""add TemplateModel

Revision ID: aa2dd6264fd3
Revises: 041177c95b30
Create Date: 2024-06-07 10:04:38.140615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'aa2dd6264fd3'
down_revision: Union[str, None] = '041177c95b30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('template',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('template_type', sa.Enum('serverless', 'pod', name='templatetypeenum'), nullable=False),
    sa.Column('compute_type', sa.Enum('nvidia_gpu', 'amd_gpu', 'cpu', name='templatecomputetypeenum'), nullable=False),
    sa.Column('container_image', sa.String(), nullable=False),
    sa.Column('container_start_command', sa.String(), nullable=True),
    sa.Column('container_disk', sa.Numeric(precision=5, scale=0), nullable=False),
    sa.Column('volume_disk', sa.Numeric(precision=5, scale=0), nullable=False),
    sa.Column('volume_mount_path', sa.String(), nullable=True),
    sa.Column('expose_http_ports', sa.String(), nullable=True),
    sa.Column('expose_tcp_ports', sa.String(), nullable=True),
    sa.Column('template_visibility', sa.Enum('public', 'private', name='templatevisibilityenum'), nullable=False),
    sa.Column('environment_variables', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('account_id', sa.UUID(), nullable=True),
    sa.Column('created_by', sa.UUID(), nullable=True),
    sa.Column('modified_by', sa.UUID(), nullable=True),
    sa.Column('created_on', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_on', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], name='fk_created_by', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['modified_by'], ['user.id'], name='fk_modified_by', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_template_created_by'), 'template', ['created_by'], unique=False)
    op.create_index(op.f('ix_template_is_deleted'), 'template', ['is_deleted'], unique=False)
    op.create_index(op.f('ix_template_modified_by'), 'template', ['modified_by'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_template_modified_by'), table_name='template')
    op.drop_index(op.f('ix_template_is_deleted'), table_name='template')
    op.drop_index(op.f('ix_template_created_by'), table_name='template')
    op.drop_table('template')
    # ### end Alembic commands ###