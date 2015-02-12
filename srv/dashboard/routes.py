from flask import render_template
from srv.dashboard import dashboard


@dashboard.route('/')
def index():
    return render_template('dashboard/index.html')