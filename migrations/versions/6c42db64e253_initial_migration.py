"""initial migration

Revision ID: 6c42db64e253
Revises: 
Create Date: 2024-12-11 08:44:09.580021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c42db64e253'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professionals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_path', sa.String(), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('socials', sa.Text(), nullable=True),
    sa.Column('banner_image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('confirm_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('banner_photo', sa.String(), nullable=True),
    sa.Column('professionals_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['professionals_id'], ['professionals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticket_class', sa.String(), nullable=False),
    sa.Column('seat', sa.String(), nullable=False),
    sa.Column('amount_paid', sa.Float(), nullable=False),
    sa.Column('qr_code', sa.String(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickets')
    op.drop_table('song_requests')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('professionals')
    # ### end Alembic commands ###
