#The request arrives at main.py first — that's the "front door." It hits the create_item function.
#It uses database.py's setup to open a connection (get a db session) — this is the "how do I even talk to the database" part.
#It uses models.py's Item blueprint to shape the data correctly — this is the "what does a valid row look like" part.
#It saves that shaped data through the open connection (db.add, db.commit).
#Response goes back.


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)  # creates the table if it doesn't exist

app = FastAPI()

# Dependency: gives each request its own DB session, closes it after
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for input
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

@app.post("/items")
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = models.Item(name=payload.name, description=payload.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()