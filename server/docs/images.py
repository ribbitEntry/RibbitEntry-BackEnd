from . import param

IMAGES_GET = {
    'tags': ['follow'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('userId', '팔로우할 유저의 이메일(아이디)')
    ],
    'responses': {
        '201': {
            'description': "팔로우 성공"
        },
        '400': {
            'description': "존재하지 않는 대상입니다."
        },
        '400': {
            'description': "JWT 인증 실패"
        }
    }
}