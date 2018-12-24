from database
from flask import request
from flasgger import swag_from
from flask_restful import Resource

from docs.login import SIGNUP_POST
from model.user import User


class SignUp(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json
        email = payload['email']
        password = payload['password']
        nickname = payload['nickname']

        if email and password and nickname:

