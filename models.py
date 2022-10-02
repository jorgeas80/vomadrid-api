from datetime import datetime

import uuid as uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'

    # Create sqlalchemy column of type uuid
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(50), nullable=False)
    original_title = Column(String(50))

    # Create sqlalchemy column of type datetime with timezone
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)


class Genre(Base):
    __tablename__ = 'genre'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)


class MovieGenre(Base):
    __tablename__ = 'movie_genre'

    movie_uuid = Column(UUID(as_uuid=True), ForeignKey('movie.uuid'), primary_key=True)
    genre_uuid = Column(UUID(as_uuid=True), ForeignKey('genre.uuid'), primary_key=True)


class MovieMetadata(Base):
    __tablename__ = 'movie_metadata'

    movie_uuid = Column(UUID(as_uuid=True), ForeignKey('movie.uuid'), primary_key=True)
    duration = Column(Integer, nullable=False)
    release_date = Column(DateTime(timezone=True), nullable=False)
    plot = Column(String(500))
    rated = Column(String(10))
    director = Column(String(50))
    cast = Column(String(500))
    # Create sqlalchemy column of type image
    poster = Column(String(500))


class MovieRating(Base):
    __tablename__ = 'movie_rating'

    movie_uuid = Column(UUID(as_uuid=True), ForeignKey('movie.uuid'), primary_key=True)
    rating = Column(Integer, nullable=False)
    votes = Column(Integer, nullable=False)
    source = Column(String(50), nullable=False)


class MovieTheaterCompany(Base):
    __tablename__ = 'movie_theater_company'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)


class MovieTheater(Base):
    __tablename__ = 'movie_theater'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(String(50), nullable=False)
    movie_theater_company_uuid = Column(UUID(as_uuid=True), ForeignKey('movie_theater_company.uuid'))


class MovieSession(Base):
    __tablename__ = 'movie_session'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    movie_uuid = Column(UUID(as_uuid=True), ForeignKey('movie.uuid'), nullable=False)
    movie_theater_uuid = Column(UUID(as_uuid=True), ForeignKey('movie_theater.uuid'), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    # Create sqlalchemy column of type url
    buy_tickets_url = Column(String(500), nullable=False)
    # Create sqlalchemy column of type boolean
    is_3d = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_imax = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_atmos = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_cinema = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4dx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_screenx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_3d = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_atmos = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_screenx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_atmos = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_screenx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_atmos_screenx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_atmos_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_screenx_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_3d_atmos_screenx_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_atmos_screenx = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_atmos_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_atmos_screenx_vision = Column(Boolean, nullable=False)
    # Create sqlalchemy column of type boolean
    is_dolby_4k_screenx_vision = Column(Boolean, nullable=False)
