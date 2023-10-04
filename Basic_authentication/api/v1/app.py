#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth to None
auth = None

# Based on the AUTH_TYPE environment variable, instantiate the proper authentication class
if getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth  # import Auth from api.v1.auth.auth
    auth = Auth()  # create an instance of Auth and assign it to auth


@app.before_request
def before_request_handler():
    """
    Handle actions before processing the request
    """
    if auth is None:
        return
    
    # List of paths that don't require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # If request path is in the excluded list, do nothing
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If authorization_header method returns None, abort with 401 error
    if auth.authorization_header(request) is None:
        abort(401)

    # If current_user method returns None, abort with 403 error
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
