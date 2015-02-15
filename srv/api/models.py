from flask_mongorest import operators
from flask_mongorest.resources import Resource

from app import db


class User(db.Document):
    email = db.EmailField(unique=True, required=True)


class Content(db.EmbeddedDocument):
    text = db.StringField()


class ContentResource(Resource):
    document = Content


class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    content = db.EmbeddedDocumentField(Content)


class PostResource(Resource):
    document = Post
    related_resources = {
        'content': ContentResource,
    }
    filters = {
        'title': [operators.Exact, operators.Startswith],
        'author_id': [operators.Exact]
    }
    rename_fields = {
        'author': 'author_id'
    }