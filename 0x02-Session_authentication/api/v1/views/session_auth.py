#!/usr/bin/env python3
""" Module that handles all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_view():
    email = request.form.get('email')
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
        if len(users) == 0:
            return jsonify({"error": "no user found for this email"}), 404
        for user in users:
            if user.is_valid_password(email):
                from api.v1.app import auth
                current_user = user
                session_id = auth.create_session(current_user.id)
                response = jsonify(current_user.to_json()), 200
                response.set_cookie(os.getenv('SESSION_NAME'), session_id)
                return response
        return jsonify({"error": "wrong password"}), 401
    except Exception as e:
        abort(401)
