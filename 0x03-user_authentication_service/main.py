#!/usr/bin/env python3
"""
Main file
"""
# import bcrypt
# passwords = []
# def encrypt_passwd(password: str) -> None:
#     passwd = password.encode('utf-8')
#     encrypted_p = bcrypt.hashpw(passwd, bcrypt.gensalt())
#     passwords.append(encrypted_p)

# def check_passwd(password: str, encrypted_p: bytes) -> None:
#     if bcrypt.checkpw(password.encode('utf-8'), encrypted_p):
#         print('Password matches!')
#     else:
#         print('Incorrect password')

# if __name__ == "__main__":
#     password = '@1234'
#     encrypt_passwd(password)
#     check_passwd(password, passwords[0])

import uuid

uid = uuid.uuid4()
print(uid)