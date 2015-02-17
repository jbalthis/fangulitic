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
import flask_debugtoolbar


# import app resources
from config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

triangle = Triangle()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    triangle.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)



    """
        TODO: Insert custom views and routing here
    """

    flask_debugtoolbar.DebugToolbarExtension(app)
    #app.session_interface = MongoEngineSessionInterface(db)

    # =======================#
    # Blueprint Registration #
    # =======================#

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app







