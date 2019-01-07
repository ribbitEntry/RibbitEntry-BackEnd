from . import param

COMMENT_POST = {
    'tags': ['my-page'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('content', '내용')
    ],
    'responses': {
        '201': {
            'description': "댓글 작성 완료"
        },
        '400': {
            'description': "JWT 인증에 실패하였거나 내용이 없습니다."
        }
    }
}
