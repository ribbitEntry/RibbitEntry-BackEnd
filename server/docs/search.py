from server.docs import param, user_example

SEARCH_GET = {
    'tags': ['search'],
    'parameters': [param('word', '검색어(사용 예시: /api/search?word=신은주열심히일해라', 'url parameter', 'str')],
    'responses': {
        '200': {'description': "검색 성공", 'example': [user_example]},
        '400': {'description': "검색어를 입력하세요."}
    }
}
