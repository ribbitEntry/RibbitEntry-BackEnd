from . import param

FOLLOW_POST = {
    'tags': ['follow'],
    'parameters': [
        param('email', "팔로우 "),
        param('password', "비밀번호")
    ],
    'responses': {
        '201': {
            'description': "JWT 반환 성공",
            "example": {
                "access_token": "dkAhffkDkanxmsJWTzhemdla",
                "refresh_token": "flvmfptlxhzms"
            }
        },
        '401': {
            'description': "없는 ID이거나 비밀번호가 틀렸습니다."
        }
    }
}

FOLLOW_DELETE = {}
