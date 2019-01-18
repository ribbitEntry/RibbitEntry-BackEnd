from server.docs import param, jwt_param, user_example

FOLLOWER_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {"now_follower": [user_example]}
        },
        '404': {'description': "없는 계정입니다."}
    }
}

FOLLOWING_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {'now_following': [user_example]}
        },
        '404': {'description': "없는 계정입니다."}
    }
}

FOLLOWING_PATCH = {
    'tags': ['follow'],
    'parameters': [
        jwt_param(),
        param('userId', '팔로우할 유저의 이메일(아이디)', 'json', 'str')
    ],
    'responses': {
        '201': {'description': "팔로우 성공"},
        '400': {'description': "존재하지 않는 대상입니다."},
        '401': {'description': "JWT 인증 실패"}
    }
}

FOLLOWING_DELETE = {
    'tags': ['follow'],
    'parameters': [
        jwt_param(),
        param('userId', '팔로우 취소할 유저의 이메일(아이디)', 'json', 'str')
    ],
    'responses': {
        '200': {'description': "팔로우 취소 성공"},
        '401': {'description': "권한이 없습니다."},
        '403': {'description': "수행할 수 없는 요청입니다. 본인 계정을 팔로우 취소할 수 없고, 피팔로워는 상대방의 팔로우에 관여할 수 없습니다."}
    }
}

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
        '400': {'description': "인자가 부족합니다."},
        '401': {'description': "없는 ID이거나 비밀번호가 틀렸습니다."}
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
        '201': {'description': '회원가입 성공'},
        '400': {'description': "인자가 부족합니다."},
        '409': {'description': '회원가입 실패(중복된 이메일)'}
    }
}

COLOR_POST = {
    'tags': ['my-page'],
    'parameters': [
        jwt_param(),
        param('color', '변경할 색', 'json', 'str')
    ],
    'responses': {
        '200': {
            'description': "색상 변경 성공",
            "example": {'color': "나는야 색상코드"}
        },
        '400': {'description': "JWT 인증에 실패하였거나 색상코드가 없습니다."}
    }
}

MY_PAGE_POST = {
    'tags': ['my-page'],
    'parameters': [
        jwt_param(),
        param('introduction', '한줄 자기소개 수정', 'form', 'str', False),
        param('nickname', '닉네임 수정', 'form', 'str', False),
        param('profile_image', '프로필 이미지 수정', 'form', 'file', False),
        param('background_image', '배경 이미지 수정', 'form', 'file', False)
    ],
    'responses': {
        '201': {'description': "마이페이지 정보 수정 성공"},
        '403': {'description': "JWT 인증 실패"},
        '406': {'description': "인자가 부족합니다."}
    }
}

USER_PAGE_GET = {
    'tags': ['user-page'],
    'responses': {
        '201': {
            'description': "유저페이지를 불러왔습니다.",
            "example": {
                "nickname": "ribbit",
                "proimg": "link",
                "backimg": "link",
                "introduction": "entry",
                "follow_num": "0",
                "follower_num": "0",
                "post": {
                    "title": "서버",
                    "content": "리빗엔트리",
                    "image": "link",
                    "user": "kim",
                    "date": "00:00:00",
                    "like": "50"
                }
            }
        }
    }
}
