#models.py works to define the structure of the database tables. It uses SQLAlchemy's ORM (Object Relational Mapper) to map Python classes to database tables. Each class represents a table, and each attribute of the class represents a column in that table. The models.py file is used by main.py to shape the data correctly when creating or querying items and users in the database.

from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)