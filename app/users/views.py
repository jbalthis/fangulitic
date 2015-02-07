from flask import Flask, Blueprint, flash, redirect, render_template, \
        request, session, url_for

from app.users import users
from app.users.decorators import login_required, admin_required
from app.users.models import db, User
from app.users.forms import *
import random
import hashlib

def check_password(plaintext, hashtext):
    salt = hashtext[0:8]
    crypted = hashtext[9:]

    if hashlib.sha512(plaintext + salt).hexdigest() == crypted:
        return True

    return False

def new_password(password):
    chars = []

    for i in range(8):
        chars.append(random.choice( \
                "0123456789abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    return "".join(chars) + '$' + \
            hashlib.sha512(password + "".join(chars)).hexdigest()

#
# Users login
#
@users.route('/users/login', methods=['GET', 'POST'])
def users_login():
    if 'logged_in' in session:
        return redirect(url_for('dashboard.dashboard_index'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                session['username'] = user.username
                session['theme'] = user.theme
                session['logged_in'] = True

                return redirect(url_for('dashboard.dashboard_index'))

    return render_template('users/login.html', form=form)

#
# Users logout
#
@users.route('/users/logout')
@login_required
def users_logout():
    session.pop('logged_in')
    session.pop('username')
    session.pop('theme')

    return redirect(url_for('users.users_login'))

@users.route('/users/changepw', methods=['GET', 'POST'])
@login_required
def users_changepw():
    form = ChangePassword()

    if form.validate_on_submit():
        oldpass = form.oldpass.data
        newpass1 = form.newpass1.data
        newpass2 = form.newpass2.data

        user = User.query.filter_by(username=session['username']).first()

        if check_password(oldpass, user.password) == False:
            flash('Password incorrect!', 'danger')

            return redirect(url_for('users.users_changepw'))

        if not newpass1 == newpass2:
            flash('New passwords do not match!', 'danger')

            return redirect(url_for('users.users_changepw'))

        if len(newpass1) <= 6:
            flash('New password is too short!', 'danger')

            return redirect(url_for('users.users_changepw'))

        user.password = new_password(newpass1)
        db.session.commit()

        flash('Your password has been changed.', 'success')
        return redirect(url_for('users.users_changepw'))
    else:
        if len(form.errors) > 0:
            flash('Have you been drinking?', 'danger')

            return redirect(url_for('users.users_changepw'))

    return render_template('users/changepw.html', theme=session['theme'], \
            form=form)

#
# Add new user
#
@users.route('/users/add', methods=['GET', 'POST'])
@login_required
@admin_required
def users_add():
    form = AddUser()

    if form.validate_on_submit():
        username = form.username.data
        password = new_password(form.password.data)
        admin = form.admin.data

        user = User.query.filter_by(username=username).first()

        if user is not None:
            flash("User '%s' already exists!" % username, 'danger')

            return redirect(url_for('users.users_add'))

        user = User(username, password, 'united', admin)
        db.session.add(user)
        db.session.commit()

        flash("User '%s' added." % username, 'success')
        return redirect(url_for('users.users_list'))
    else:
        if len(form.errors) > 0:
            flash('Please fill out the fucking form.', 'danger')
            return render_template('users/add.html', \
                    theme=session['theme'], form=form)

    return render_template('users/add.html', theme=session['theme'], \
            form=form)

#
# Modify user
#
@users.route('/users/modify', methods=['GET', 'POST'])
@login_required
@admin_required
def users_modify():
    form = ModifyUser()

    if form.validate_on_submit():
        user = User.query.filter_by( \
                username=form.username.data).first()

        if user is None:
            return redirect(url_for('users.users_list'))

        if user.username == 'admin':
            flash('You cannot modify the fucking christ user.', 'danger')

            return redirect(url_for('users.users_list'))

        if form.password.data is not None:
            user.password = new_password(form.password.data)

        user.admin = form.admin.data

        db.session.commit()

        flash("User '%s' was modified." % form.username.data, 'warning')
        return redirect(url_for('users.users_list'))

    form.username.data = request.args['user']

    user = User.query.filter_by(username=form.username.data).first()

    if user is None:
        return redirect(url_for('users.users_list'))

    if user.username == 'admin':
        flash('You cannot modify the fucking christ user.', 'danger')

        return redirect(url_for('users.users_list'))

    form.admin.data = user.admin

    return render_template('users/modify.html', theme=session['theme'], \
            form=form)

#
# Remove user
#
@users.route('/users/remove')
@login_required
@admin_required
def users_remove():
    username = request.args['user']

    user = User.query.filter_by(username=username).first()

    if user is None:
        flash('No such user.', 'danger')
        return redirect(url_for('users.users_list'))

    if user.id == 1:
        flash('You cannot remove the fucking christ user.', 'danger')

        return redirect(url_for('users.users_list'))

    if user.username == session.get('username'):
        flash('Do not remove yourself, you dumb shit.', 'danger')
        return redirect(url_for('users.users_list'))

    db.session.delete(user)
    db.session.commit()

    flash("User '%s' was removed." % user.username, 'danger')
    return redirect(url_for('users.users_list'))

#
# List all users
#
@users.route('/users/list')
@login_required
@admin_required
def users_list():
    users = User.query.all()

    return render_template('users/list.html', theme=session['theme'], \
            users=users)
