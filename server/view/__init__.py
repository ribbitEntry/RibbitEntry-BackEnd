from flask import Flask
from flask_restful import Api


class Router():
    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def register(self):
        from view.login import Login
        self.api.add_resource(Login, '/api/login')

        from view.signUp import SignUp
        self.api.add_resource(SignUp, '/api/sign-up')

        from view.web import Web
        self.api.add_resource(Web, '/server-status')
