from monkful.resources import MongoEngineResource
from app.documents import Post
from app.serializers import PostSerializer


class PostResource(MongoEngineResource):
    document = Post
    serializer = PostSerializer


