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

from passlib.context import CryptContext

Base.metadata.create_all(bind=engine)  # creates the table if it doesn't exist

app = FastAPI()

# Dependency: gives each request its own DB session, closes it after
def get_db():
    db = SessionLocal()
    try:
        yield db #it will yield the db session to the request, and then close it after the request is done. This is important because we don't want to keep the db session open for too long, as it can cause issues with the database connection pool.
    finally:
        db.close()

# Pydantic model for input
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None  #it will allow the description to be optional, so that we can create an item without a description. If the description is not provided, it will be set to None.

#Create an item in the database, return the created item
@app.post("/items")
def create_item(payload: ItemCreate, db: Session = Depends(get_db)): #it will create a new item in the database, and return the created item. It will use the ItemCreate model to validate the input data, and it will use the get_db dependency to get a db session.
    item = models.Item(name=payload.name, description=payload.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#get all items from the database, return a list of items
@app.get("/items")
def list_items(db: Session = Depends(get_db)): #it will get all the items from the database, and return a list of items. It will use the get_db dependency to get a db session.
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

#for PATCH, we can use the same ItemUpdate model, but we will only update the fields that are provided in the request. 
# If a field is not provided, we will leave it unchanged.
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

#for user signup, we will create a new user in the database with a hashed password. 
# We will use the passlib library to hash the password.
class UserCreate(BaseModel):
    email: str
    password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #it will use bcrypt to hash the password, and will automatically handle the salt for us.

#it will check if the email is already registered, if it is, it will return a 400 error.
@app.post("/signup")
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = pwd_context.hash(payload.password) #it will hash the password using bcrypt, and will automatically handle the salt for us.
    user = models.User(email=payload.email, hashed_password=hashed_pw) #it will create a new user with the hashed password
    db.add(user) #it will add the new user to the database
    db.commit() #it will commit the transaction to the database
    db.refresh(user) #it will refresh the user object with the data from the database, so that we can return the id and email of the new user.
    return {"id": user.id, "email": user.email} #it will return the id and email of the new user, but not the password, because we don't want to expose the password to the client.


#it will check if the email and password are correct, if they are, it will return a success message. If they are not, it will return a 401 error.
class UserLogin(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(payload: UserLogin, db: Session = Depends(get_db)):  #it will check the user's credentials
    user = db.query(models.User).filter(models.User.email == payload.email).first() #it will query the database for a user with the provided email. If no user is found, it will return None.

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not pwd_context.verify(payload.password, user.hashed_password): #it will verify the provided password against the hashed password stored in the database. If the password is incorrect, it will return False.
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"message": "Login successful"}


















#person.age         age value stored inside person
#person.walk()      hey person run your walk() method


#thing.something
#means: "go inside thing, and give me something."
#If something is a plain value → you're reading/writing data (item.name)
#If something is followed by () → you're calling a function that belongs to that object (db.commit())