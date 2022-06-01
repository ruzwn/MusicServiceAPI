import models, schemas

from sqlalchemy.orm import Session


def get_all_songs(db: Session):
    return db.query(models.Song).all()


def get_song_by_id(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def create_song(db: Session, song: schemas.SongCreate):
    db_song = models.Song(name=song.name,
                          release_date=song.release_date,
                          album_id=song.album_id,
                          genre_id=song.genre_id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def delete_song(db: Session, song: schemas.Song):
    songs_artists = db.query(models.ArtistHasSong).filter(models.ArtistHasSong.song_id == song.id).all()
    for song_artist in songs_artists:
        db.delete(song_artist)
        db.commit()
    db.delete(song)
    db.commit()
    return song
