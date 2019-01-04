# from database import db_session
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.view import unicode_safe_json_dumps, upload_files
from server.extensions import db
from server.model.user import User
from server.model.post import Post
from server.model.comment import Comment
from server.docs.myPage import MY_PAGE_GET, MY_PAGE_POST


class MyPage(Resource):

    @swag_from(MY_PAGE_GET)
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

    # 마이페이지 정보 수정(닉네임, 프로필 이미지, 배경 이미지)
    @swag_from(MY_PAGE_POST)
    @jwt_required
    def post(self):

        userId = get_jwt_identity()
        profile_image = request.files.get('profile_image')
        background_image = request.files.get('background_image')
        try:
            nickname = request.form['nickname']
        except:
            nickname = None

        try:
            introduction = request.form['introduction']
        except:
            introduction = None

        user = User.query.filter(User.id == userId).first()

        if userId and user:

            if profile_image or background_image or nickname or introduction:

                if profile_image:
                    user.proimg = upload_files(profile_image, userId, various='profile')

                if background_image:
                    user.backimg = upload_files(background_image, userId, various='background')

                if nickname:
                    user.nickname = nickname

                if introduction:
                    user.introduction = introduction

                db.session.commit()
                return unicode_safe_json_dumps({"status": "프로필 정보 변경 성공"}, 201)

            else:
                return {"status": "argument required"}, 406

        else:
            return {"status": "invalid authentication"}, 403
