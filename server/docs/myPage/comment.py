from docs import param, jwt_param

COMMENT_POST = {
    'tags': ['my-page'],
    'parameters': [
        jwt_param(),
        param('content', '내용', 'json', 'str')
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
