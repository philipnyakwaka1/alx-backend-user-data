#!/usr/bin/env python3
"""Module for SessionAuth class
"""
from . import auth
import uuid


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
