from docs import param

LOGIN_POST = {
    'tags': ['login'],
    'parameters': [
        param('userId', "아이디", 'json', 'str'),
        param('password', "비밀번호", 'json', 'str')
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
        '400': {
            'description': "인자가 부족합니다."
        },
        '401': {
            'description': "없는 ID이거나 비밀번호가 틀렸습니다."
        }
    }
}

SIGNUP_POST = {
    'tags': ['login'],
    'parameters': [
        param('userId', '아이디', 'json', 'str'),
        param('password', '비밀번호', 'json', 'str'),
        param('nickname', '닉네임', 'json', 'str')
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '400': {
            'description': "인자가 부족합니다."
        },
        '409': {
            'description': '회원가입 실패(중복된 이메일)'
        }
    }
}
