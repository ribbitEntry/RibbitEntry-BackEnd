# 복잡한 파라미터를 한 줄로 줄여주는 함수
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


user_example = {
    "userId": "DSM2018",
    "nickname": "대마대마",
    "profile_image": "http://ribbit.jaehoon.kim:5000/api/images?userId=DSM2018&profile=DSM2018.jpg"
}

user_detail_example = {
    'user_info': {
        "nickname": "ribbit",
        "profile_image": "link",
        "back_image": "link",
        "introduction": "entry",
        "follow_num": "0",
        "follower_num": "0"
    }
}
