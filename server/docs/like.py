LIKE_PATCH = {
    'tags': ['posts'],
    'response' :  {
        '201': {
            'description': "좋아요 성공",
            "example": {'like': "좋아요 갯수"}
        },
        '400': {
            'description': "좋아요 실패, 글이 없는 글이에요."
        }
    }
}
