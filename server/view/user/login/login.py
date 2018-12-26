from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from server.docs.login import LOGIN_POST
from server.extensions import db
from server.model.user import User


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        userId = payload['userId']
        password = payload['password']

        if userId and password:
            if User.query.filter(User.id == userId).first():
                return {
                    'access_token': create_access_token(),
                    'refresh_token': create_refresh_token(),
                    'color_set'
                }
