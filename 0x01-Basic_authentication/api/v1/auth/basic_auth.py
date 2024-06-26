#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from . import auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(auth.Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 encoding part
        """
        tmp = authorization_header
        if tmp is None or type(tmp) != str or tmp[:6] != 'Basic ':
            return None
        return tmp[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Returns decoded value
        """
        tmp = base64_authorization_header
        if tmp is None or type(tmp) != str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Return username and password
        """
        tmp = decoded_base64_authorization_header
        if tmp is None or type(tmp) != str or ':' not in tmp:
            return (None, None)
        data = tmp.split(':')
        return (data[0], data[1])

    @staticmethod
    def user_object_from_credentials(user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return user object
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
            if len(users) == 0:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception as e:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        """
        auth_header = self.authorization_header(request)
        base_64_header = self.extract_base64_authorization_header(auth_header)
        decoded_h = self.decode_base64_authorization_header(base_64_header)
        user_c = self.extract_user_credentials(decoded_h)
        user = self.user_object_from_credentials(user_c[0], user_c[1])
        return user
