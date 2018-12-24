from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from view import Router
from config.config import Config


def create_app():
    app = Flask(__name__)

    Router(app).register()
    app.config.from_object(Config)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
