from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request
from flasgger import swag_from
from flask_restful import Resource

from server.model.user import User
from server.view import unicode_safe_json_dumps, upload_files
from server.extensions import db
from server.docs.myPage import MY_PAGE_POST


# 마이페이지 정보 수정(닉네임, 프로필 이미지, 배경 이미지)\
class MyPagePatch(Resource):

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
