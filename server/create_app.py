from flask import Flask
from flasgger import Swagger

from config.config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
