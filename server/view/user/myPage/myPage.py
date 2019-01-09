import os
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, current_app, jsonify
from flasgger import swag_from
from flask_restful import Resource

from server.model.user import User
from server.view import upload_files
from server.extensions import db
from server.docs.myPage.myPage import MY_PAGE_POST


# 마이페이지 정보 수정(닉네임, 프로필 이미지, 배경 이미지)
class MyPagePatch(Resource):

    @swag_from(MY_PAGE_POST)
    @jwt_required
    def patch(self, userId):

        user_id = get_jwt_identity()
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

        user = User.query.filter(User.id == user_id).first()

        if user_id and user and user_id == userId:

            if profile_image or background_image or nickname or introduction:

                if profile_image:
                    path = current_app.config['UPLOAD_FOLDER_PATH'] + '/{}/profile/{}'.format(userId, user.proimg)
                    if os.path.isfile(path):
                        os.remove(path)
                    user.proimg = upload_files(profile_image, userId, various='profile')

                if background_image:
                    path = current_app.config['UPLOAD_FOLDER_PATH'] + '/{}/background/{}'.format(userId, user.backimg)
                    if os.path.isfile(path):
                        os.remove(path)
                    user.backimg = upload_files(background_image, userId, various='background')

                if nickname:
                    user.nickname = nickname

                if introduction:
                    user.introduction = introduction

                db.session.commit()
                return jsonify({"status": "프로필 정보 변경 성공"}, 201)

            else:
                return {"status": "argument required"}, 406

        else:
            return {"status": "invalid authentication"}, 403
