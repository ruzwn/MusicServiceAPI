from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/songs/", response_model=list[schemas.Song])
def get_all_songs(db: Session = Depends(get_db)):
    songs = crud.get_all_songs(db=db)
    return songs


@app.get("/songs/{song_id}", response_model=schemas.Song)
def get_song_by_id(song_id: int, db: Session = Depends(get_db)):
    song = crud.get_song_by_id(db=db, song_id=song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@app.post("/songs/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return crud.create_song(db=db, song=song)


@app.delete("/songs/{song_id}", response_model=schemas.Song)
def delete_song(song_id: int, db: Session = Depends(get_db)):
    song = crud.get_song_by_id(db=db, song_id=song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return crud.delete_song(db=db, song=song)
