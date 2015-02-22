"""
    app - app/__init__.py
    the application package constructor
"""

# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_triangle import Triangle
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
import flask_debugtoolbar

# import app resources
from config import config

triangle = Triangle()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    # app init
    app = Flask(__name__)

    # config init
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # extensions init
    triangle.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    # debug toolbar init
    flask_debugtoolbar.DebugToolbarExtension(app)

    # =======================#
    # Blueprint Registration #
    # =======================#

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    return app

