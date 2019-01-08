from docs import param

IMAGES_GET = {
    'tags': ['images'],
    'parameters': [
        param('userId', '유저아이디', 'url', 'str', False),
        param('postId', '게시글 고유번호', 'url', 'str', False),
        param('fileId', '파일 위치', 'url', 'str', False),
        param('profile', '프로필', 'url', 'str', False),
        param('background', '배경 이미지', 'url', 'str', False)
    ],
    'responses': {
        '200': {
            'description': "파일 반환 성공"
        }
    }
}
