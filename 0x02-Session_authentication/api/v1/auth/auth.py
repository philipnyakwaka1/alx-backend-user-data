#!/usr/bin/env python3
"""Module for Auth class"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header
        """
        auth = request.headers.get('Authorization')
        if auth is None or request is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        """
        return None

    def session_cookie(self, request=None):
        """Returns cookie value from a request
        """
        if request is None:
            return None
        cookie = os.getenv('SESSION_NAME')
        _my_session_id = request.cookies.get(cookie)
        return _my_session_id
