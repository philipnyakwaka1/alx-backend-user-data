#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, request, jsonify, abort
from typing import List, Tuple
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route('/', strict_slashes=False, methods=['GET'])
def home_page() -> Tuple[dict, int]:
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', strict_slashes=False, methods=['POST'])
def users():
    """register user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.register_user(email, password)
        return jsonify(
            {"email": f"{user.email}", "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', strict_slashes=False, methods=['POST'])
def login() -> str:
    """login function
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not auth.valid_login(email, password):
        abort(401)
    session_id = auth.create_session(email)
    resp = jsonify({"email": f"{email}", "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
