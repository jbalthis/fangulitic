from flask import Blueprint

users = Blueprint('users', __name__)

import app.modules.users.views
