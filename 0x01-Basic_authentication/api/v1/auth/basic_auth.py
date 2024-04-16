#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from . import auth


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
