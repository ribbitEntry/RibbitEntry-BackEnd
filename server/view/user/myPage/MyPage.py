# from database import db_session
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.docs.myPage import MY_PAGE_GET
from server.model.user import User
from server.model.post import Post
from server.model.comment import Comment


class MyPage(Resource):

    @swag_from(MY_PAGE_GET)
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user_info = User.query.filter(User.id == user_id).first()
        post_info = Post.query.filter(user=user_id).all()
        comment_info = Comment.query.filter()
        if user_info:
            return {
                "nickname": user_info.nickname,
                "profile_image": user_info.proimg,
                "background_image": user_info.backimg,
                "introduction": user_info.introduction,
                "follow_num": user_info.follow_num,
                "follower_num": user_info.follower_num,
                "post": [{
                    "title": post.title,
                    "content": post.content,
                    "image": post.image,
                    "user": post.user,
                    "date": post.date,
                    "like": post.like,
                    "comment": [{
                        "title": comment.title,
                        "content": comment.content,
                        "date": comment.date} for comment in comment_info]
                } for post in post_info]
            }
        else:
            pass
