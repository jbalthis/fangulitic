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
#app.config.from_object('app.config')

# create db
db = MongoEngine()




from srv import dashboard

app.register_blueprint(dashboard.dashboard)

from srv import users
app.register_blueprint(users.users)

from srv import metrics
app.register_blueprint(metrics.metrics)