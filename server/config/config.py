import os
from datetime import timedelta


class Config(object):
    SWAGGER = {
        'title': 'RibbitEntry',
        'specs_route': '/api/docs',
        'uiversion': 3,

        'info': {
            'title': 'RibbitEntry-Backend API',
            'version': '0.1',
            'description': 'Ribbit 프로젝트의 백엔드 API 명세서입니다.'
        },
        'host': 'aws.jaehoon.kim:5000',
        'basePath': '/api/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'login',
                'description': '로그인/회원가입'
            },
            {
                'name': 'my-page',
                'description': '마이페이지 정보'
            },
            {
                'name': 'follow',
                'description': '팔로잉/팔로워 관리'
            },
            {
                'name': 'posts',
                'description': '게시글'
            },

            {
                'name': 'search',
                'description': '검색'
            },

            {
                'name': 'main-page',
                'description': '메인화면'
            }
        ]
    }

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1224@ribbit.jaehoon.kim/ribbit-entry'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 상용운전시 환경변수 필히 설정할 것!!
    SECRET_KEY = os.getenv('SECRET_KEY', 'NEEDFORSPEED')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'GAE1GUL')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
