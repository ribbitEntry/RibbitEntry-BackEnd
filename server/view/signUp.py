from flask_restful import Resource
from flasgger import swag_from

from docs.login import SIGNUP_POST


class SignUp(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):
        pass
