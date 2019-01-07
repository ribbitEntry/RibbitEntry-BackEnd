from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.view import unicode_safe_json_dumps
from server.model.user import User
from server.model.post import Post
from server.docs.userpage import USER_PAGE_GET


class UserPage(Resource):

    @swag_from(USER_PAGE_GET)
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user_info = User.query.filter(User.id == user_id).first()
        post_info = Post.query.filter(Post.user == user_id).all()

        user_info_ = {
            "nickname": user_info.nickname,
            "profile_image": user_info.proimg,
            "background_image": user_info.backimg,
            "introduction": user_info.introduction,
            "follow_num": user_info.follow_num,
            "follower_num": user_info.follower_num
        }

        if not user_info:
            return {"status": "invalid authentication"}, 401

        elif user_info and not post_info:
            return unicode_safe_json_dumps({"user_info": user_info_})

        elif user_info and post_info:
            return unicode_safe_json_dumps({
                "user_info": user_info_,
                "post": [
                    {
                        "content": posts.content,
                        "image": posts.image,
                        "user": posts.user,
                        "date": str(posts.date),
                        "like": posts.like
                    } for posts in post_info]
            }, 200)
