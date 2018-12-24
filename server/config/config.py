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
                'name': 'main_page',
                'description': '메인화면'
            }
        ]
    }

    JSON_AS_ASCII = False
