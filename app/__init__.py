#!/usr/bin/env python2

from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask.ext.sqlalchemy import SQLAlchemy

csrf = CsrfProtect()
app = Flask(__name__)
csrf.init_app(app)
app.config.from_object('app.config')
db = SQLAlchemy(app)
