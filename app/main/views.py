"""
    main.views - app/main/views.py
    main app views
"""

from datetime import datetime
from flask import render_template, redirect, session, url_for

from . import main
from .forms import NameForm
from .. import db
from ..documents import User


@main.route('/', methods=['GET', 'POST'])
def index():

    form = NameForm()
    if form.validate_on_submit():

        return redirect(url_for('.index'))
    return render_template(
        'main/index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False),
        current_time=datetime.utcnow()
    )