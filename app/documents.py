from mongoengine import Document, fields

class User(Document):
    user_id = fields.StringField()

class Role(Document):
    role_id = fields.StringField()

class Post(Document):
    post_id = fields.StringField()
    author = fields.StringField()
    title = fields.StringField()
    slug = fields.StringField()
    tags = fields.ListField(fields.StringField())
    body = fields.StringField()