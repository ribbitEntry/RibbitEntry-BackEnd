from flask_restful import Resource
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.docs.mainPage.mainpage import MAIN_PAGE_GET
from server.model.post import Post
from server.model.user import User
from server.model.follow import Follow
from server.view import unicode_safe_json_dumps


class MainPage(Resource):
    @swag_from(MAIN_PAGE_GET)
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user_info = User.query.filter(User.id == user_id).first()

        post_info = Post.query.filter(Follow.follow == user_id).filter(Post.user == Follow.follower).order_by().all()

        user_info_ = {
            "user_id" : user_info.id,
            "nickname": user_info.nickname,
            "profile_image": user_info.proimg,
            "background_image": user_info.backimg,
            "introduction": user_info.introduction,
            "follow_num": user_info.follow_num,
            "follower_num": user_info.follower_num
        }

        if not user_info:
            return {"status": "없는 유저입니다."}, 401

        elif user_info and not post_info:
            return unicode_safe_json_dumps({"user_info": user_info_}, 200)

        elif user_info and post_info:
            return unicode_safe_json_dumps({
                       "user_info": user_info_,
                       "post": [
                           {
                               "id": posts.post_id,
                               "content": posts.content,
                               "image": posts.image,
                               "user": posts.user,
                               "nickname": User.query.filter(User.id == posts.user).first().nickname,
                               "profile_image": User.query.filter(User.id == posts.user).first().proimg,
                               "date": str(posts.date),
                               "like": posts.like
                           } for posts in post_info]
                   }, 200)
