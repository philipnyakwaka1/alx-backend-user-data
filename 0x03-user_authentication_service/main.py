#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """Tests register user end-point
    """
    payload = {'email': email, 'password': password}
    resp = requests.post('http://localhost:5000/users', data=payload)
    assert resp.status_code == 200
    assert resp.json().get('email') == email
    dup = resp = requests.post('http://localhost:5000/users', data=payload)
    assert resp.status_code == 400


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests for incorrect credentials login
    """
    payload = {'email': email, 'password': password}
    resp = requests.post('http://localhost:5000/sessions', data=payload)
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """Tests valid login
    """
    payload = {'email': email, 'password': password}
    resp = requests.post('http://localhost:5000/sessions', data=payload)
    assert resp.status_code == 200
    assert resp.json().get('message') == 'logged in'
    return resp.cookies.get('session_id')


def profile_unlogged() -> None:
    """Tests unlogged profile
    """
    resp = requests.get('http://localhost:5000/profile')
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """Tests for logged profile
    """
    cookies = dict(session_id=session_id)
    resp = requests.get('http://localhost:5000/profile', cookies=cookies)
    assert resp.status_code == 200


def log_out(session_id: str) -> None:
    """Tests for logout
    """
    cookies = dict(session_id=session_id)
    resp = requests.delete('http://localhost:5000/sessions', cookies=cookies)
    assert resp.json().get('message') == 'Bienvenue'
    assert resp.status_code == 200


def reset_password_token(email: str) -> str:
    """tests for reset password token
    """
    payload = {'email': email}
    resp = requests.post('http://localhost:5000/reset_password', data=payload)
    assert resp.status_code == 200
    assert resp.json().get('reset_token') is not None


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests for update password
    """
    payload = {'email': email,
               'reset_token': reset_token, 'new_password': new_password}
    resp = requests.put('http://localhost:5000/reset_password', data=payload)
    assert resp.status_code == 200
    assert resp.json().get('message') == 'Password updated'


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
