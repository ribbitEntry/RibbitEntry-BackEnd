from flask_restful import Resource
from flasgger import swag_from

from server.docs.posts import POST_POST, POST_DELETE


class Post(Resource):

    @swag_from(POST_POST)
    def post(self):
        pass

    @swag_from(POST_DELETE)
    def delete(self):
        pass
