from . import param

MY_PAGE_POST = {
    'tags': ['my-page'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('profile-image', "프로필 이미지", required=False),
        param('background-imgae', "(프로필)배경 이미지", required=False),
        param('introduction', '한줄 자기소개', required=False),
    ],
    'responses': {
        '201': {
            'description': "마이페이지 정보 수정 성공",
        },
        '403': {
            'description': "JWT 인증 실"
        }
    }
}

MY_PAGE_GET = {
    'tags': ['my-page'],
    'parameters': [
            param('id', "user_id"),
        ],
    'responses': {
        '201': {
            'description': "마이페이지를 불러왔습니다.",
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
                        "like": "50",
                        "comment": {
                                    "title": "서버",
                                    "content": "리빗엔트리",
                                    "date": "00:00:00"
                        }
                }
            }
        },
        '404': {
            'description': "없는 유저입니다.",
        }
    }
}