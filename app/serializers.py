from monkful.serializers import Serializer, fields


class PostSerializer(Serializer):
    post_id = fields.StringField()


