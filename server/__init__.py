from flask import Flask


def create_app():
    app = Flask(__name__)

    from server.view import Router
    Router(app).register()

    from server.config.config import Config
    app.config.from_object(Config)

    register_extensions(app)
    return app


def register_extensions(app: Flask):
    from server import extensions
    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.db.create_all(app=app)
    extensions.jwt.init_app(app)
    extensions.swagger.init_app(app)
    extensions.swagger.template = app.config['SWAGGER_TEMPLATE']
