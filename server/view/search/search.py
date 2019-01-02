from flask_restful import Resource
from flasgger import swag_from
from flask import request

from server.docs.search import SEARCH_POST
from server.model.user import User
from server.view import unicode_safe_json_dumps


class Search(Resource):

    @swag_from(SEARCH_POST)
    def post(self):
        search_word = request.json['search_word']
        user_info = User.query.filter(User.nickname == search_word).first()

        if user_info:
            return unicode_safe_json_dumps({
                "nickname": user_info.nickname,
                "profile_image": user_info.proimg
            }, 200)

        else:
            return unicode_safe_json_dumps({"status": "없는 유저입니다."}, 404)
