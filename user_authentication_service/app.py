#!/usr/bin/env python3
"""flask module
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def register_user():
    """Register a user and respond with a status message."""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Check if a user exists and validate the password."""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        abort(400)

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)

@app.route('/sessions', methods=['DELETE'])
def logout():
    """Find the user with the requested session ID. If the user exists destroy
    the session and redirect the user to GET /. If the user does not exist,
    respond with a 403 HTTP status.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Find the user with the requested session ID. If the user exists, respond
    with a 200 HTTP status and a JSON payload of the user's email. If the user
    does not exist, respond with a 403 HTTP status.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Generate a reset password token and respond with a 200 HTTP status and a
    JSON payload of the reset token. If the email is not registered, respond
    with a 403 HTTP status.
    """
    email = request.form.get('email')

    if email is None:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


def update_password():
    """Update a user's password and respond with a 200 HTTP status and a JSON
    payload of the user's email. If the reset token is invalid, respond with a
    403 HTTP status.
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if email is None or reset_token is None or new_password is None:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
