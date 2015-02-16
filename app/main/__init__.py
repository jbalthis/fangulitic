"""
    main - app/main/__init__.py
    main module constructor
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors