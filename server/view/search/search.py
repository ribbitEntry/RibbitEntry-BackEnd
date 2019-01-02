from flask_restful import Resource
from flasgger import swag_from
from flask import request

from server.docs.search import SEARCH_POST
from server.model.user import User
from server.model.post import Post


class Search(Resource):

    @swag_from(SEARCH_POST)
    def post(self):
        search_word = request.json['search_word']
        user_info = User.query.filter(search_word == User.id)
        post_info = User.query.filter(search_word == Post.title)

        user_info_ = {
            "nickname": user_info.nickname,
            "profile_image": user_info.proimg,
            "introduction": user_info.introduction,
            "follow_num": user_info.follow_num,
            "follower_num": user_info.follower_num
        }

        post_info_ = {
            "title": post_info.title,
            "user": post_info.user,
            "date": post_info.date
        }

        if user_info:

            if post_info:
                return {
                    "user_info": user_info_,
                    "post_info": post_info_
                }

            else:
                return {
                    "user_info": user_info_
                }

        else:
            return {"status": "없는 검색어입니다."}, 404