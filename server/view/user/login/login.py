from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from server.docs.login import LOGIN_POST
from server.model.user import User
from server.view.user.login import validate_email


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        userId = payload['userId']
        password = payload['password']

        if userId and password:
            if validate_email(email=userId):
                if User.query.filter(User.id == userId).first():
                    return {
                        'access_token': create_access_token(identity=userId),
                        'refresh_token': create_refresh_token(identity=userId),
                        'color_set': 'processing'
                    }, 200
                else:
                    return Response("없는 계정이거나 잘못된 비밀번호")
            else:
                return Response("유효하지 않은 이메일"), 405
        else:
            return {"status": "incorrectly authentication info"}, 401
