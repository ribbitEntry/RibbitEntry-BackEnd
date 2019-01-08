from docs import param

SEARCH_GET = {
    'tags': ['search'],
    'parameters': [
        {
            'name': 'word',
            'description': "검색어(사용 예시: /api/search?word=신은주열심히일해라",
            'in': 'url parameter',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': "검색 성공",
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