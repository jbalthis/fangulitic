"""
    app - app/__init__.py
    the application package constructor
"""

# import libraries
from flask import Flask
#from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_mongoalchemy import MongoAlchemy
from flask_triangle import Triangle
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
import flask_debugtoolbar


# import app resources
from config import config


triangle = Triangle()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = MongoAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

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

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app







