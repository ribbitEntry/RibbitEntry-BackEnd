from flask import request
from flasgger import swag_from
from flask_restful import Resource

from server.extensions import db
from server.docs.login import SIGNUP_POST
from server.model.user import User
from server.view.user.login import validate_email


class SignUp(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json
        email = payload['userId']
        password = payload['password']
        nickname = payload['nickname']

        if email and password and nickname:

            if validate_email(email) and User.query.filter(User.id == email).first():
                return {"status": "The ID already exists."}, 409

            else:
                user = User(id=email, pw=password, nickname=nickname, theme_color='default')
                db.session.add(user)
                db.session.commit()
                return {"status": "sign-up has been succeeded"}, 201
