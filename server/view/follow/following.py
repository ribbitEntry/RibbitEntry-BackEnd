from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from server.docs.follow import FOLLOW_GET, FOLLOW_POST, FOLLOW_DELETE


class Follow(Resource):

    @jwt_required
    @swag_from(FOLLOW_GET)
    def get(self):
        pass

    @jwt_required
    @swag_from(FOLLOW_POST)
    def post(self):
        pass

    @jwt_required
    @swag_from(FOLLOW_DELETE)
    def delete(self):
        pass
