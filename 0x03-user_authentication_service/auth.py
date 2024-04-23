#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _generate_uuid() -> str:
    """Generates unique id
    """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes a password
    """
    passwd = password.encode('utf-8')
    hashed_passwd = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return hashed_passwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register new user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {user.email} already exists')
        except NoResultFound:
            hashed_p = _hash_password(password)
            user = self._db.add_user(email, hashed_p)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """validates user credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            hashed_p = user.hashed_password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_p):
                return True
            return False
        except NoResultFound:
            return False
