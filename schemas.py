from datetime import date

from pydantic import BaseModel


class SongBase(BaseModel):
    name: str
    release_date: date
    album_id: int
    genre_id: int


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True
