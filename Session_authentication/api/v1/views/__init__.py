#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Flask, Blueprint
from .session_auth import session_auth  # Use a relative import here

app = Flask(__name__)
app.register_blueprint(session_auth)

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)