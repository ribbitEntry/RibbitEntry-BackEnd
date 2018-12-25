from . import param

POST_POST = {
    'tags': ['posts'],
    'parameters': [
        param('title', "제목"),
        param('content', "내용"),
        param('image', "이미지")
    ],
    'responses': {
        '201': {
            'description': "글 작성 성공",
        },
        '400': {
            'description': "제목, 내용을 모두 채워주세요."
        }
    }
}

POST_DELETE = {
    'tags': ['posts'],
    'parameters': [
        param('post_id', "제목")
    ],
    'responses': {
        '200': {
            'description': "글 삭제 성공",
        }
    }
}