from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from . import db

class User(db.Document):
    password_hash = db.StringField(max_length=128)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Document):
    role_id = db.StringField()


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