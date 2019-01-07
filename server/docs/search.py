from . import param

SEARCH_POST = {
    'tags': ['search'],
    'parameters': [
        param('search_word', "검색어"),
    ],
    'responses': {
        '200': {
            'description': "검색 성",
            'example': [
                {
                    'user_id': 'dsm2018@gmail.com',
                    'nickname': '대마고',
                    'profile_image': 'http://ribbit.jaehoon.kim:5000/api/user/profile-image/dsm2018'
                }
            ]
        },
        '400': {
            'description': "검색어를 입력하세요."
        }
    }
}