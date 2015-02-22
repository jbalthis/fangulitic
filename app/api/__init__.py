"""
    app.api - app/api/__init__.py
    api module init
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, comments, decorators, errors, posts, users