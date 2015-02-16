from monkful.serializers import Serializer, fields


class PostSerializer(Serializer):
    post_id = fields.StringField()
    author = fields.StringField()
    title = fields.StringField()
    slug = fields.StringField()
    tags = fields.ListField(fields.StringField())
    body = fields.StringField()



