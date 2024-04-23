#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, request, jsonify
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
