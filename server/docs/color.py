from . import param

COLOR_POST = {
    'tags': ['my-page'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('color', '변경할 색')
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
