# api/v1/views/__init__.py
from flask import Blueprint
from . import session_auth

app_views = Blueprint('app_views', __name__)
