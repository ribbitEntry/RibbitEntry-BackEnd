from . import param

SEARCH_POST = {
    'tags': ['search'],
    'parameters': [
        param('search_word', "검색어"),
    ],
    'responses': {
        '200': {
            'description': "검색시작",
        },
        '400': {
            'description': "검색어를 입력하세요."
        }
    }
}

SEARCH_GET = {
    'tags': ['search'],
    'parameters': [
        param('search_word', "검색어"),
    ],
    'responses': {
        '200': {
            'description': "검색완료.",
            "example": {
                "nickname": "닉네임",
                "id": "아이디",
                "proimg": "프로필사진",
                "title": "글 제목"
            }
        },
        '404': {
            'description': "없는 검색어입니다."
        }
    }
}