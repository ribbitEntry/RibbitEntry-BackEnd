from flask import request
from flasgger import swag_from
from flask_restful import Resource

from server.extensions import db
from server.docs.login import SIGNUP_POST
from server.model.user import User
# from server.view.user.login import validate_email


class SignUp(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json
        user_id = payload['id']
        password = payload['password']
        nickname = payload['nickname']
        if user_id and password and nickname:

            if User.query.filter(User.id == user_id).first():
                return {"status": "The ID already exists."}, 409

            else:
                user = User(id=user_id, pw=password, nickname=nickname, theme_color='default')
                db.session.add(user)
                db.session.commit()
                return {"status": "sign-up has been succeed"}, 201

        else:
            return {"status": "Not enough factors."}, 400
