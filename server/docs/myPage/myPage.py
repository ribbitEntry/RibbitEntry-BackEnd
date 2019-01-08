from docs import param

MY_PAGE_POST = {
    'tags': ['my-page'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'introduction',
            'description': "한줄 자기소개 수정",
            'in': 'form',
            'type': 'str',
            'required': False
        },
        {
            'name': 'nickname',
            'description': "닉네임 수정",
            'in': 'form',
            'type': 'str',
            'required': False
        },
        {
            'name': 'profile_image',
            'description': "프로필 이미지 수정",
            'in': 'form',
            'type': 'file',
            'required': False
        },
        {
            'name': 'background_image',
            'description': "배경 이미지 수정",
            'in': 'form',
            'type': 'file',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': "마이페이지 정보 수정 성공",
        },
        '403': {
            'description': "JWT 인증 실패"
        },
        '406': {
            'description': "인자가 부족합니다."
        }
    }
}
