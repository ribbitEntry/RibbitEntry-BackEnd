from . import param

FOLLOW_GET = {
    'tags': ['follow'],
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
            'description': "팔로우 정보 반환 성공",
            'example': {
                'now_following': [
                    '김재훈', '김준우', '신은주', '이채은'
                ],
                'now_follower': [
                    '김재훈', '김준우', '신은주', '이채은'
                ]
            }
        },
        '403': {
            'description': "JWT 인증 실패"
        }
    }
}

FOLLOW_POST = {
    'tags': ['follow'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('userId', '팔로우할 유저의 이메일(아이디)')
    ],
    'responses': {
        '201': {
            'description': "팔로우 성공",
        },
        '403': {
            'description': "JWT 인증 실패"
        }
    }
}

FOLLOW_DELETE = {
    'tags': ['follow'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('userId', '팔로우 취소할 유저의 이메일(아이디)')
    ],
    'responses': {
        '200': {
            'description': "팔로우 취소 성공",
        },
        '403': {
            'description': "JWT 인증 실패"
        }
    }
}
