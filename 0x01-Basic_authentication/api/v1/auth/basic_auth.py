#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from . import auth
import base64


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
