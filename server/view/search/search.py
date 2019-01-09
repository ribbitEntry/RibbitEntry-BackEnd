from flask_restful import Resource
from flasgger import swag_from
from flask import request, jsonify

from server.docs.search.search import SEARCH_GET
from server.model.user import User


class Search(Resource):

    @swag_from(SEARCH_GET)
    def get(self):
        search_word = request.args.get('word')
        user_info = User.query.filter(User.nickname == search_word).all()

        if user_info:
            return jsonify(
                [
                    {
                        "nickname": user.nickname,
                        "profile_image": user.proimg,
                        "user_id": user.id
                    } for user in user_info], 200)

        else:
            return jsonify({"status": "없는 유저입니다."}, 404)
