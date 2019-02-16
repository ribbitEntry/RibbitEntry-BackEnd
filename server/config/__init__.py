import os

from datetime import timedelta


class Config:
    SERVICE_NAME = "Ribbitentry-Backend",
    SERVICE_NAME_UPPER = "RIBBITENTRY-BACKEND"

    RUN_SETTING = {'threaded': True}

    SWAGGER = {
        'title': "Ribbitentry-Backend",
        'specs_route': '/api/docs',
        'uiversion': 3,

        'info': {
            'title': 'Ribbitentry-Backend API',
            'version': '0.1',
            'description': 'Ribbit 프로젝트의 백엔드 API 명세서입니다.'
        },
        'basePath': '/api/',
    }

    JSON_AS_ASCII = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1224@ribbit.jaehoon.kim/ribbit-entry'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 상용운전시 환경변수 필히 설정할 것!!
    SECRET_KEY = os.getenv('SECRET_KEY', 'NEEDFORSPEED')

    JWT_HEADER_TYPE = 'JWT'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'GAE1GUL')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=12)

    # FILE UPLOAD CONFIGS(MUST BE CHANGED!)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'resource')

    # ONLY FOR UBUNTU
    # TODO 운영체제별 의존성 제거 및 상대 경로로 변경
    UPLOAD_FOLDER_PATH = '/home/ubuntu/RibbitEntry-BackEnd/resource'
    ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'bmp', 'gif', 'png')
