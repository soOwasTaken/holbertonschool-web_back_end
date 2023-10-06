#!/usr/bin/env python3
"""
session_auth module flask blueprint
"""
from flask import Blueprint, jsonify, request, abort, make_response
from models.user import User
from os import getenv

session_auth = Blueprint('session_auth', __name__, url_prefix='/auth_session')


@session_auth.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle POST /auth_session/login route.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(user.to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
