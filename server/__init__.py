from flask import Flask


def register_extensions(app: Flask):
    from server import extensions

    extensions.swagger.template = app.config['SWAGGER_TEMPLATE']

    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.jwt.init_app(app)
    extensions.swagger.init_app(app)


def utility(app: Flask):
    from view import Router

    Router(app).register()

    from config.config import Config

    app.config.from_object(Config)


def create_app():
    app = Flask(__name__)

    return app
