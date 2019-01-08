from server.docs import param

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