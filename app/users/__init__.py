from flask import Flask, Blueprint

users = Blueprint('users', __name__)

import app.users.models
import app.users.forms
import app.users.decorators
import app.users.views
