from flask import Flask


def create_app():
    app = Flask(__name__)

    from server.config import Config
    app.config.from_object(Config)

    from server.view import Router
    Router(app).register()

    from server import extensions
    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.db.create_all(app=app)
    extensions.jwt.init_app(app)
    extensions.swagger.init_app(app)

    return app
