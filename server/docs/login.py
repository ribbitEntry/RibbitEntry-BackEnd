from . import param

LOGIN_POST = {
    'tags': ['login'],
    'parameters': [
        param('email', "이메일"),
        param('password', "비밀번호")
    ],
    'responses': {
        '200': {
            'description': "JWT 반환 성공",
            "example": {
                "access_token": "dkAhffkDkanxmsJWTzhemdla",
                "refresh_token": "flvmfptlxhzms",
                "color_set": "yellow"
            }
        },
        '401': {
            'description': "없는 ID이거나 비밀번호가 틀렸습니다."
        }
    }
}

SIGNUP_POST = {
    'tags': ['login'],
    'parameters': [
        param('email', '이메일'),
        param('password', '비밀번호'),
        param('nickname', '닉네임')
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '409': {
            'description': '회원가입 실패(중복된 이메일)'
        }
    }
}
