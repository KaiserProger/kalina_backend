"""Only one migration

Revision ID: e0fd8b06380d
Revises: 
Create Date: 2023-04-26 07:11:10.529500

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0fd8b06380d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('scores', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('phone')
    )
    op.create_table('Revision',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('shop_address', sa.String(), nullable=True),
    sa.Column('expire_date', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.phone'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Attachment',
    sa.Column('revision_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('media_type', sa.Enum('Audio', 'Image', 'Form', name='mediaenum'), nullable=True),
    sa.Column('attachment_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['revision_id'], ['Revision.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Form',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('revision_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('is_template', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['revision_id'], ['Revision.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Task',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('form_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('task_content', sa.String(), nullable=True),
    sa.Column('task_type', sa.Enum('MultiSelect', 'SingleSelect', 'SingleLine', 'MultiLine', name='tasktypeenum'), nullable=True),
    sa.Column('answers', sa.ARRAY(sa.String(), dimensions=1, zero_indexes=True), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['Form.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Task')
    op.drop_table('Form')
    op.drop_table('Attachment')
    op.drop_table('Revision')
    op.drop_table('User')
    # ### end Alembic commands ###