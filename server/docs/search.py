from . import param

SEARCH_POST = {
    'tags': ['search'],
    'parameters': [
        param('search_word', "검색어"),
    ],
    'responses': {
        '200': {
            'description': "검색시작",
            'example': [
                {
                    'userId': 'dsm2018@gmail.com',
                    'nickname': '대마고',
                    'profile_image': 'http://ribbit.jaehoon.kim:5000/api/user/profile-image/dsm2018',
                    'following': [
                        {
                            'nickname': '곰돌이1'
                        }
                    ],
                    'follower': [
                        {
                            'nickname': '곰돌이2'
                        }
                    ]
                }
            ]
        },
        '400': {
            'description': "검색어를 입력하세요."
        }
    }
}