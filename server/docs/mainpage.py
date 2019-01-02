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
        '201': {
            'description': "메인페이지를 불러왔습니다.",
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
        }
    }
}
