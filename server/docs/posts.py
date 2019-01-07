from . import param

POST_POST = {
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
            'name': 'file',
            'description': "배열 형태의 파일",
            'in': 'from',
            'type': 'file',
            'required': True
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

POST_DELETE = {
    'tags': ['posts'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('post_id', "제목")
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
