#The request arrives at main.py first — that's the "front door." It hits the create_item function.
#It uses database.py's setup to open a connection (get a db session) — this is the "how do I even talk to the database" part.
#It uses models.py's Item blueprint to shape the data correctly — this is the "what does a valid row look like" part.
#It saves that shaped data through the open connection (db.add, db.commit).
#Response goes back.


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException


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

#Create an item in the database, return the created item
@app.post("/items")
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    item = models.Item(name=payload.name, description=payload.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#get all items from the database, return a list of items
@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

#search for an item by id, if not found, return 404
@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

#delete an item by id, if not found, return 404
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted"}


#Update an item by id, if not found, return 404
class ItemUpdate(BaseModel):
    name: str
    description: Optional[str] = None

@app.patch("/items/{item_id}")
def patch_item(item_id: int, payload: ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = payload.name
    item.description = payload.description

    db.commit()
    db.refresh(item)
    return item

#person.age         age value stored inside person
#person.walk()      hey person run your walk() method


#thing.something
#means: "go inside thing, and give me something."
#If something is a plain value → you're reading/writing data (item.name)
#If something is followed by () → you're calling a function that belongs to that object (db.commit())