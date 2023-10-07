#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Flask, Blueprint
from models.user import User


app = Flask(__name__)

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.session_auth import *
from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
