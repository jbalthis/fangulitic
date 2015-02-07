from flask import Flask, Blueprint, redirect, render_template, session, \
        request, url_for

from app.dashboard import dashboard
from app.users.decorators import login_required
from app.users.models import db, User

from app.astores.models import aStore
from app.customs.models import CustomSite
#from app.replicated.models import ReplicatedSite
from app.wordpress.models import WordPress

VALID_THEMES = [
        'amelia', 'cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly',
        'journal', 'lumen', 'readable', 'simplex', 'slate', 'spacelab',
        'superhero', 'united', 'yeti' ]

@dashboard.route('/')
@login_required
def dashboard_index():
    user = User.query.filter_by(username=session['username']).first()

    return render_template('dashboard/index.html', \
            theme=session['theme'], admin=user.admin, \
            astores=aStore.query.count(), \
            customs=CustomSite.query.count(), \
            wordpress=WordPress.query.count())

@dashboard.route('/search')
@login_required
def dashboard_search():
    # u mad? :)
    return redirect('http://lmgtfy.com/?q='+request.args['q'])

@dashboard.route('/theme/<theme>')
@login_required
def dashboard_theme(theme):
    if not theme in VALID_THEMES:
        return redirect(url_for('dashboard.dashboard_index'))

    user = User.query.filter_by(username=session['username']).first()
    user.theme = theme
    db.session.commit()

    session['theme'] = user.theme

    return redirect(url_for('dashboard.dashboard_index'))
