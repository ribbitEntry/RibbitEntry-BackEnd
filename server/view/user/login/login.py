from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from server.docs.login.login import LOGIN_POST
from server.model.user import User
# from server.view.user.login import validate_email


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        userId = payload['userId']
        password = payload['password']
        valid_user = User.query.filter(User.id == userId).first()

        if userId and password:
            if valid_user and valid_user.pw == password:
                return {
                           'access_token': create_access_token(identity=userId),
                           'refresh_token': create_refresh_token(identity=userId),
                           'color_set': User.query.filter(User.id == userId).first().theme_color
                       }, 200
            else:
                return {"status": "Account is missing or incorrect password"}, 401
        else:
            return {"status": "Not enough factors."}, 400
