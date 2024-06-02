from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a model class inheriting from Base
class User(Base):

    __tablename__ = 'users'  # Name of the table in the database

    id = Column(Integer, primary_key=True)  # Define columns
    name = Column(String)
    email = Column(String)