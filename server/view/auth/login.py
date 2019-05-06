from flask import request, abort
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from docs.user import LOGIN_POST
from server.model.user import User


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        valid_user = User.query.filter(User.id == payload['user_id'] and User.pw == payload['password']).first()

        return {
                   'access_token': create_access_token(identity=payload['user_id']),
                   'refresh_token': create_refresh_token(identity=payload['user_id']),
                   'color_set': User.query.filter(User.id == payload['user_id']).first().theme_color
               }, 200 if valid_user else abort(401)
