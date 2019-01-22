import socket

from server.config import Config


class ProductionConfig(Config):
    # get host ip(???)
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5000
    DEBUG = False

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })

    Config.SWAGGER['host'] = '{}:{}'.format(Config.DOMAIN or HOST, PORT)
