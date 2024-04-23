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

"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))    