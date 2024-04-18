#!/usr/bin/env python3
"""Module for SessionAuth class
"""
from . import auth
import uuid
from models.user import User


class SessionAuth(auth.Auth):
    """Session class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user_id based on session_id"""
        if session_id is None or type(session_id) != str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """Returns user id
        """
        _my_session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(_my_session_id)
        user = User.get(user_id)
        return user
