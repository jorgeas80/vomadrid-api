"""Create models

Revision ID: 22760624030a
Revises: 
Create Date: 2022-10-03 00:35:53.753600

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '22760624030a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('movie',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('original_title', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('movie_theater_company',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('movie_genre',
    sa.Column('movie_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('genre_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['genre_uuid'], ['genre.uuid'], ),
    sa.ForeignKeyConstraint(['movie_uuid'], ['movie.uuid'], ),
    sa.PrimaryKeyConstraint('movie_uuid', 'genre_uuid')
    )
    op.create_table('movie_metadata',
    sa.Column('movie_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('release_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('plot', sa.String(length=500), nullable=True),
    sa.Column('rated', sa.String(length=10), nullable=True),
    sa.Column('director', sa.String(length=50), nullable=True),
    sa.Column('cast', sa.String(length=500), nullable=True),
    sa.Column('poster', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['movie_uuid'], ['movie.uuid'], ),
    sa.PrimaryKeyConstraint('movie_uuid')
    )
    op.create_table('movie_rating',
    sa.Column('movie_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['movie_uuid'], ['movie.uuid'], ),
    sa.PrimaryKeyConstraint('movie_uuid')
    )
    op.create_table('movie_theater',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('zip_code', sa.String(length=50), nullable=False),
    sa.Column('movie_theater_company_uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['movie_theater_company_uuid'], ['movie_theater_company.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('movie_session',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('movie_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('movie_theater_uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('start_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('buy_tickets_url', sa.String(length=500), nullable=False),
    sa.Column('is_3d', sa.Boolean(), nullable=False),
    sa.Column('is_imax', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_atmos', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_cinema', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4dx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_screenx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_3d', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_atmos', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_screenx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_atmos', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_screenx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_atmos_screenx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_atmos_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_screenx_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_3d_atmos_screenx_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_atmos_screenx', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_atmos_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_atmos_screenx_vision', sa.Boolean(), nullable=False),
    sa.Column('is_dolby_4k_screenx_vision', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['movie_theater_uuid'], ['movie_theater.uuid'], ),
    sa.ForeignKeyConstraint(['movie_uuid'], ['movie.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_session')
    op.drop_table('movie_theater')
    op.drop_table('movie_rating')
    op.drop_table('movie_metadata')
    op.drop_table('movie_genre')
    op.drop_table('movie_theater_company')
    op.drop_table('movie')
    op.drop_table('genre')
    # ### end Alembic commands ###
