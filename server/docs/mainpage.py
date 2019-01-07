from . import param

MAIN_PAGE_GET = {
    'tags': ['main-page'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '메인 포스트가 없는 경우 유저 정보만 반환합니다.',
            'example': {
                'user_info': {
                    "nickname": "ribbit",
                    "profile_image": "link",
                    "back_image": "link",
                    "introduction": "entry",
                    "follow_num": "0",
                    "follower_num": "0"
                }
            }
        },
        '200': {
            'description': "메인포스트가 있는 경우 유저 정보와 메인 포스트 둘 다 반환합니다.",
            "example": {
                'user_info': {
                    "nickname": "ribbit",
                    "profile_image": "link",
                    "back_image": "link",
                    "introduction": "entry",
                    "follow_num": "0",
                    "follower_num": "0"
                },
                "post": {
                    "title": "서버",
                    "content": "리빗엔트리",
                    "image": "link",
                    "user": "kim",
                    "date": "00:00:00",
                    "like": "50"
                }
            }
        },
        '401': {
            'description': '없는 유저입니다.'
        }
    }
}
