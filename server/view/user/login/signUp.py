from flask import request
from flasgger import swag_from
from flask_restful import Resource

from extensions import db
from server.docs.login import SIGNUP_POST
from server.model.user import User


class SignUp(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json
        email = payload['email']
        password = payload['password']
        nickname = payload['nickname']

        if email and password and nickname:

            if User.query.filter(User.id == email).first():
                return {"status": "The ID already exists."}, 409

            else:
                user = User(id=email, password=password, nickname=nickname)
                db.session.add(user)
                db.session.commit()
                return {"status": "sign-up has been succeeded"}
