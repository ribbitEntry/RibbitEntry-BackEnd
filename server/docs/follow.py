from . import param

FOLLOWER_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {
                'now_follower': [
                    '김재훈', '김준우', '신은주', '이채은'
                ]
            }
        },
        '404': {
            'description': "없는 계정입니다."
        }
    }
}

FOLLOWING_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {
                'now_following': [
                    '김재훈', '김준우', '신은주', '이채은'
                ]
            }
        },
        '404': {
            'description': "없는 계정입니다."
        }
    }
}

FOLLOWING_PATCH = {
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
            'description': "팔로우 성공"
        },
        '400': {
            'description': "존재하지 않는 대상입니다."
        },
        '400': {
            'description': "JWT 인증 실패"
        }
    }
}

FOLLOWING_DELETE = {
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
        '401': {
            'description': "권한이 없습니다."
        },
        '403': {
            'description': "수행할 수 없는 잘못된 요청입니다. 본인 계정을 팔로우 취소할 수 없고, 피팔로워는 상대방의 팔로우에 관여할 수 없습니다."
        }
    }
}
