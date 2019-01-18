import os
from datetime import timedelta


# TODO Config 클래스를 상속하는 타 클래스를 만들어 실행 환경 별 설정을 달리함
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

    # TODO 스웨거 템플릿 태그 설정 삭제
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
            },

            {
                'name': 'user-page',
                'description': '유저페이지'
            },

            {
                'name': 'images',
                'description': '이미지'
            }
        ]
    }

    JSON_AS_ASCII = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1224@ribbit.jaehoon.kim/ribbit-entry'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 상용운전시 환경변수 필히 설정할 것!!
    SECRET_KEY = os.getenv('SECRET_KEY', 'NEEDFORSPEED')

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'GAE1GUL')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=12)

    # FILE UPLOAD CONFIGS(MUST BE CHANGED!)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'resource')

    # ONLY FOR UBUNTU
    # TODO 운영체제별 의존성 제거 및 상대 경로로 변경
    UPLOAD_FOLDER_PATH = '/home/ubuntu/RibbitEntry-BackEnd/resource'
    ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'bmp', 'gif', 'png')
