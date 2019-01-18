from server.docs import param

POSTS_POST = {
    'tags': ['posts'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': "게시글 내용",
            'in': 'form',
            'type': 'str',
            'required': True
        },
        {
            'name': 'file[1]',
            'description': "첫번째 파일",
            'in': 'from',
            'type': 'file',
            'required': False
        },
        {
            'name': 'file[2]',
            'description': "두번째 파일",
            'in': 'from',
            'type': 'file',
            'required': False
        },
        {
            'name': 'file[3]',
            'description': "세번째 파일",
            'in': 'from',
            'type': 'file',
            'required': False
        },
        {
            'name': 'file[4]',
            'description': "네번째 파일",
            'in': 'from',
            'type': 'file',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': "글 작성 완료",
        },
        '400': {
            'description': "내용을 작성해주세요."
        },
        '401': {
            'description': "일치하지 않는 인증 정보입니다."
        }
    }
}

POST_ELEMENT_GET = {
    'tags': ['posts'],
    'responses': {
        '200': {
            'description': "글 조회 성공"
        },
        '400': {
            'description': "존재하지 않는 게시글의 번호입니다."
        }
    }
}

POST_ELEMENT_DELETE = {
    'tags': ['posts'],
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
            'description': "글 삭제 성공"
        },
        '400': {
            'description': "없는 글입니다."
        }
    }
}

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

from server.docs import param, jwt_param

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
