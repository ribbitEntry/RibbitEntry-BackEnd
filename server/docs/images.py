from . import param

IMAGES_POST = {
    'tags': ['my-page'],
    'parameters': [
        {
            'name': 'userId',
            'description': "유저아이디",
            'in': 'url',
            'type': 'str',
            'required': False
        },
        {
            'name': 'postId',
            'description': "게시글 고유번호",
            'in': 'url',
            'type': 'str',
            'required': False
        },
        {
            'name': 'fileId',
            'description': "파일 위치",
            'in': 'url',
            'type': 'str',
            'required': False
        },
        {
            'name': 'profile',
            'description': "프로필",
            'in': 'url',
            'type': 'str',
            'required': False
        },
        {
            'name': 'background',
            'description': "배경 이미지",
            'in': 'url',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': "파일 반환 성공"
        }
    }
}
