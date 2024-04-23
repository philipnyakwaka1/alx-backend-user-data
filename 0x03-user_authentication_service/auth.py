#!/usr/bin/env python3
"""DB module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password
    """
    passwd = password.encode('utf-8')
    hashed_passwd = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return hashed_passwd
