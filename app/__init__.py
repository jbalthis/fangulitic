"""
    app - app/__init__.py
    the application package constructor
"""

# import libraries
from flask import Flask
from flask_restful import Api
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_triangle import Triangle
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

# import app resources
from config import config
from resources import PostResource

triangle = Triangle()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
toolbar = DebugToolbarExtension()
api = Api()
db = MongoEngine()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    triangle.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)
    api.init_app(app)
    db.init_app(app)

    """
        TODO: Insert custom views and routing here
    """

    app.session_interface = MongoEngineSessionInterface(db)

    api.add_resource(PostResource, '/posts/', '/posts/<string:post_id>/', endpoint='post_ep')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app







