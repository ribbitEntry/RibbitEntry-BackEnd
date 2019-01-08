from . import param, jwt_param

FOLLOWER_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {
                "now_follower": [
                    {
                        "userId": "by09115",
                        "nickname": "덩어리덩어리",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=by09115&profile=WIN_20180923.jpg"
                    },
                    {
                        "userId": "sineunjoo",
                        "nickname": "개구리지롱",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=sineunjoo&profile=Gaegul.jpg"
                    },
                    {
                        "userId": "DSM2018",
                        "nickname": "대마대마",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=DSM2018&profile=DSM2018.jpg"
                    }
                ]
            }
        }
    },
    '404': {
        'description': "없는 계정입니다."
    }
}

FOLLOWING_GET = {
    'tags': ['follow'],
    'responses': {
        '200': {
            'description': "팔로우 정보 반환 성공",
            'example': {
                'now_following': [
                    {
                        "userId": "김재훈",
                        "nickname": "덩어리덩어리",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=by09115&profile=WIN_20180923.jpg"
                    },
                    {
                        "userId": "신은주",
                        "nickname": "개구리지롱",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=sineunjoo&profile=Gaegul.jpg"
                    },
                    {
                        "userId": "김준우",
                        "nickname": "대마대마",
                        "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=DSM2018&profile=DSM2018.jpg"
                    }
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
        jwt_param(),
        param('userId', '팔로우할 유저의 이메일(아이디)', 'json', 'str')
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
        jwt_param(),
        param('userId', '팔로우 취소할 유저의 이메일(아이디)', 'json', 'str')
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
