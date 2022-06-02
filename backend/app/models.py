from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    info = Column(String)
    label_id = Column(Integer, ForeignKey("labels.id"))


class ArtistHasSong(Base):
    __tablename__ = "artist_has_song"

    artist_id = Column(Integer, ForeignKey("artists.id", ondelete="CASCADE"), primary_key=True)
    song_id = Column(Integer, ForeignKey("songs.id", ondelete="CASCADE"), primary_key=True)


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="CASCADE"))

    artists = relationship("Artist", secondary=ArtistHasSong.__tablename__, passive_deletes=True)


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    info = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class ListeningHistory(Base):
    __tablename__ = "listening_histories"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True,)
    song_id = Column(Integer, ForeignKey("songs.id", ondelete="CASCADE"), primary_key=True)
    listening_time = Column(Date, nullable=False)


class PlaylistHasSong(Base):
    __tablename__ = "playlist_has_song"

    playlist_id = Column(Integer, ForeignKey("playlists.id", ondelete="CASCADE"), primary_key=True)
    song_id = Column(Integer, ForeignKey("songs.id", ondelete="CASCADE"), primary_key=True)


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    info = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    reg_date = Column(DateTime, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    gender = Column(String)
    country = Column(String)
