# import libraries
from flask import Flask
from flask_triangle import Triangle
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine



# create app
app = Flask(__name__)

Triangle(app)
Bootstrap(app)


# config
# TODO: place in external config file
app.debug = True
app.config['SECRET_KEY'] = '1234567890abcdefghijklmnopqrstuvwxyz'
toolbar = DebugToolbarExtension(app)
# app.config.from_object('app.config')
app.config.update(
    MONGODB_HOST='localhost',
    MONGODB_PORT='27017',
    MONGODB_DB='fangulitic_db',
)


# create db
db = MongoEngine(app)


from srv import dashboard
app.register_blueprint(dashboard.dashboard)

from srv import users
app.register_blueprint(users.users)

from srv import metrics
app.register_blueprint(metrics.metrics)