from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from config.config import Config


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(Config)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    from view.login import Login
    api.add_resource(Login, '/api/login')

    from view.web import Web
    api.add_resource(Web, '/server-status')

    return app
