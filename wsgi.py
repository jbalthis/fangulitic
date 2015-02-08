
from datetime import datetime

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'This is where the magic is happening at (%s)' % datetime.now('%Y-%m-%d %H:%M:S')

