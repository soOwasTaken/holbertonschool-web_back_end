#!/usr/bin/env python3
"""
SessionAuth module
"""
from flask import Flask, request, jsonify
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from api.v1.app import auth  # Import auth where it's needed, not at top
from models.user import User  # Replace this import with your actual User class

app = Flask(__name__)

@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """
    Handles session authentication login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    
    if not password:
        return jsonify({"error": "password missing"}), 400
    
    users = User.search({'email': email})
    
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    
    user = users[0]  # Assuming search returns a list, adjust if necessary
    
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    # Assuming you have auth and create_session properly set up
    session_id = auth.create_session(user.id)  # Replace user.id with actual user ID field
    response = jsonify(user.to_json())  # Assuming to_json is a valid method on your User
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    
    return response