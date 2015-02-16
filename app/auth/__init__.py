"""
    app.auth - app/auth/__init__.py
    auth module
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views