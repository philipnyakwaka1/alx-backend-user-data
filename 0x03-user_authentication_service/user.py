#!/usr/bin/env python3
"""Module for User class
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import urllib.parse
import os

load_dotenv()
DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DB = os.getenv('DB')
password = urllib.parse.quote_plus(PASSWORD)

url = f'mysql+mysqldb://{DB_USER}:{password}@{HOST}/{DB}'
engine = create_engine(url)
Base = declarative_base()


class User(Base):
    """class for the User model"""
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(250), nullable=False)
    hashed_password = Column('hashed_password', String(250), nullable=False)
    session_id = Column('session_id', String(250), nullable=False)
    reset_token = Column('reset_token', String(250), nullable=False)


Base.metadata.create_all(bind=engine)
