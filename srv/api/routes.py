from flask_mongorest.views import ResourceView
from flask_mongorest import methods

from srv.api import api
from srv.api.models import PostResource


@api.register(name='posts', url='/posts/')
class PostView(ResourceView):
    resource = PostResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]