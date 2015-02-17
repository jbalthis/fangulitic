from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from . import db
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.StringField(max_length=128)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class Page(db.Document):
    page_id = db.StringField


class Post(db.Document):
    created_at = db.CreatedField()
    slug = db.StringField(max_length=255, required=True)
    title = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.DocumentField("Comment"))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    #meta = {
    #    'allow_inheritance': True,
    #    'indexes': ['-created_at', 'slug'],
    #    'ordering': ['-created_at']
    #}


class Comment(db.Document):
    created_at = db.CreatedField()
    body = db.StringField(required=True)
    author = db.StringField(max_length=255, required=True)