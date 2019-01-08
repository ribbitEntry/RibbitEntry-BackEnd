def param(name, description, in_, type_, required=True):
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type_,
        'required': required
    }


def jwt_param():
    return {
        'name': 'Authorization',
        'description': 'JWT 인증 토큰',
        'in': 'header',
        'type': 'str',
        'required': True
    }
