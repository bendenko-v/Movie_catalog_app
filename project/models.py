from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(5000))
    trailer = Column(String(200))
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer(), ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = Column(Integer(), ForeignKey("directors.id"))
    director = relationship("Director")


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    name = Column(String(100))
    surname = Column(String(200))
    favorite_genre = Column(String(200))


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()


movie_schema = MovieSchema()
director_schema = DirectorSchema()
genre_schema = GenreSchema()
user_schema = UserSchema()
