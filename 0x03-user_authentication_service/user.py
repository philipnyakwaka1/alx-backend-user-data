#!/usr/bin/env python3
"""Module for User class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """class for the User model"""
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(250), nullable=False)
    hashed_password = Column('hashed_password', String(250), nullable=False)
    session_id = Column('session_id', String(250))
    reset_token = Column('reset_token', String(250))
