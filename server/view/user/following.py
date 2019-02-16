from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.docs.user import FOLLOWER_GET, FOLLOWING_GET, FOLLOWING_PATCH, FOLLOWING_DELETE
from server.model.user import User
from server.model.follow import Follow
from server.extensions import db
from server.view import unicode_safe_json_dumps


class Follower(Resource):

    @swag_from(FOLLOWER_GET)
    def get(self, userId):
        # 자신을 팔로우하고 있는 팔로워의 목록을 확인
        if userId and User.query.filter(User.id == userId).first():
            follower = Follow.query.filter(Follow.follower == userId).all()
            return unicode_safe_json_dumps(
                {
                    "now_follower": [
                        {
                            "userId": er.follow,
                            "nickname": User.query.filter(User.id == er.follow).first().nickname,
                            "profile_image": User.query.filter(User.id == er.follow).first().proimg
                        } for er in follower
                    ]
                }
            )


class Following(Resource):

    @swag_from(FOLLOWING_GET)
    def get(self, userId):

        # 만약 userId 가 있고 일치한 회원정보가 있을 경우 해당 회원의 팔로워 반환
        if userId and User.query.filter(User.id == userId).first():
            following = Follow.query.filter(Follow.follow == userId).all()

            return unicode_safe_json_dumps(
                {
                    "now_following": [
                        {
                            "userId": ing.follower,
                            "nickname": User.query.filter(User.id == userId).first().nickname,
                            "profile_image": User.query.filter(User.id == userId).first().proimg
                        } for ing in following
                    ]
                }, 200
            )

        else:
            return {"status": "invalid authentication"}, 401

    @jwt_required
    @swag_from(FOLLOWING_PATCH)
    def patch(self, userId):
        own_user = get_jwt_identity()
        be_followed = userId

        user_query = User.query.filter(User.id == own_user).first()
        passive_user_query = User.query.filter(User.id == be_followed).first()

        if own_user and not user_query:
            return {"status": "invalid authentication"}, 401

        elif own_user and user_query and not passive_user_query:
            return {"status": "invalid passive user info"}, 400

        elif own_user and user_query and passive_user_query:

            if not Follow.query.filter(Follow.follow == own_user, Follow.follower == be_followed).first():
                be_followed_set = Follow(follow=own_user, follower=be_followed)
                db.session.add(be_followed_set)
                user_query.follow_num += 1
                passive_user_query.follower_num += 1
                db.session.commit()
            return {"status": "It was succeed that adding follow info"}, 201

    @jwt_required
    @swag_from(FOLLOWING_DELETE)
    def delete(self, userId):
        be_deleted = request.json['userId']
        user_query = User.query.filter(User.id == userId).first()
        passive_user_query = User.query.filter(User.id == be_deleted).first()

        if userId == be_deleted:
            return unicode_safe_json_dumps({"status": "잘못된 요청입니다. 본인 계정을 팔로우 취소할 수 없습니다."}, 403)

        elif userId == Follow.query.filter(Follow.follower == userId).first():
            return unicode_safe_json_dumps({"status": "수행할 수 없는 명령입니다.(피팔로워는 상대방의 팔로우에 관여할 수 없음)"}, 403)

        elif userId and User.query.filter(User.id == userId).first():
            be_deleted_info = Follow.query.filter(Follow.follow == userId,
                                                  Follow.follower == be_deleted).first()
            db.session.delete(be_deleted_info)

            user_query.follow_num -= 1
            passive_user_query.follower_num -= 1

            db.session.commit()
            return {"status": "It was succeed that deleting follow info"}, 200

        else:
            return {"status": "invalid authentication"}, 401
