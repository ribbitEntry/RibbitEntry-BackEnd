from flask_restful import Resource
from flasgger import swag_from

from server.docs.login import LOGIN_POST


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        pass
