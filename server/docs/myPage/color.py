from docs import param, jwt_param

COLOR_POST = {
    'tags': ['my-page'],
    'parameters': [
        jwt_param(),
        param('color', '변경할 색', 'json', 'str')
    ],
    'responses': {
        '200': {
            'description': "색상 변경 성공",
            "example": {'color': "나는야 색상코드"}
        },
        '400': {
            'description': "JWT 인증에 실패하였거나 색상코드가 없습니다."
        }
    }
}
