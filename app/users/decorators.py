from functools import wraps
from flask import request, redirect, session, url_for
from app.users.models import User

def login_required(f):
    @wraps(f)

    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
                return redirect(url_for('users.users_login'))

        return f(*args, **kwargs)

    return decorated_function

def admin_required(f):
    @wraps(f)

    def decorated_function(*args, **kwargs):
        user = User.query.filter_by(username=session['username']).first()

        if user.admin == False:
            return redirect(url_for('dashboard.dashboard_index'))

        return f(*args, **kwargs)

    return decorated_function
