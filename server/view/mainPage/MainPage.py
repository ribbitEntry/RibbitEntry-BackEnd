from flask_restful import Resource
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.docs.mainpage import MAIN_PAGE_GET
from server.model.post import Post
from server.model.user import User
from server.model.comment import Comment


class MainPage(Resource):

    @swag_from(MAIN_PAGE_GET)
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user_info = User.quere.filter(User.id == user_id)
        post_info = User.quere.fiflter(Post.user == user_id)

        user_info_ = {
            "nickname": user_info.nickname,
            "profile_image": user_info.proimg,
            "introduction": user_info.introduction,
            "follow_num": user_info.follow_num,
            "follower_num": user_info.follower_num
        }

        if not user_info:
            return {"status": "없는 유저입니다."}, 401

        elif user_info and not post_info:
            return {"user_info": user_info_}, 200

        elif user_info and post_info:
            return {
                       "user_info": user_info_,
                       "post": [
                           {
                               "title": posts.title,
                               "content": posts.content,
                               "image": posts.image,
                               "user": posts.user,
                               "date": posts.date,
                               "like": posts.like,
                               "comment": [
                                   {
                                       "comment_id": Comment.query.filter(comment_id=comment).first().comment_id,
                                       "user": Comment.query.filter(comment_id=comment).first().user,
                                       "title": Comment.query.filter(comment_id=comment).first().title,
                                       "content": Comment.query.filter(comment_id=comment).first().content,
                                       "date": Comment.query.filter(comment_id=comment).first().date
                                   } for comment in posts.comment]
                           } for posts in post_info]
                   }, 200
