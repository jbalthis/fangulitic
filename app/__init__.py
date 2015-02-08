# import libraries
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine


# import local modules
from app.modules import dashboard, users


# create app
app = Flask(__name__)


app.debug = True
app.config['SECRET_KEY'] = '1234567890abcdefghijklmnopqrstuvwxyz'
toolbar = DebugToolbarExtension(app)

# register module blueprints
app.register_blueprint(dashboard)
app.register_blueprint(users)

app.config.from_object('app.config')

db = MongoEngine()

@app.route('/')
def index():
    return render_template('base.html')