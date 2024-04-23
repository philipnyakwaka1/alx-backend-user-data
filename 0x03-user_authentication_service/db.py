#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import bcrypt
from user import User
from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds new user to db
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, *args, **kwargs) -> User:
        """Filters a user
        """
        for key, val in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError('Invalid attribute')
            user = self._session.query(
                User).filter(getattr(User, key) == val).first()
        if user is None:
            raise NoResultFound('User not found')
        return user

    def update_user(self, user_id, **kwargs):
        """Updates user attributes
        """
        user = self._session.query(User).filter(User.id == user_id).first()
        if user is None:
            raise NoResultFound('No User matching the id')
        for key, val in kwargs.items():
            if not hasattr(User, key):
                raise ValueError('Attribute does not exist')
            setattr(user, key, val)
        self._session.commit()
