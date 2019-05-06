from docs import jwt_param, user_detail_example

MAIN_PAGE_GET = {
    'tags': ['main-page'],
    'parameters': [jwt_param()],
    'responses': {
        '200': {
            'description': '메인 포스트가 없는 경우 유저 정보만 반환합니다.',
            'example': user_detail_example
        },
        '200': {
            'description': "메인포스트가 있는 경우 유저 정보와 메인 포스트 둘 다 반환합니다.",
            "example": {
                'user_info': user_detail_example,
                "post": {
                    "content": "리빗엔트리",
                    "image": "link",
                    "user": "kim",
                    "nickname": "바보",
                    "proimg": "이미지",
                    "date": "00:00:00",
                    "like": "50"
                }
            }
        },
        '401': {'description': '없는 유저입니다.'}
    }
}
