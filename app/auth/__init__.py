"""
    app.auth - app/auth/__init__.py
    auth module init
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views, forms