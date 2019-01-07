from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.docs.follow import FOLLOW_GET, FOLLOW_POST, FOLLOW_DELETE
from server.model.user import User
from server.model.follow import Follow
from server.view import unicode_safe_json_dumps
from server.extensions import db


class Following(Resource):

    @swag_from(FOLLOW_GET)
    def get(self, userId):

        # 만약 userId 가 있고 일치한 회원정보가 있을 경우 해당 회원의 팔로워 반환
        if userId and User.query.filter(User.id == userId).first():
            follower = Follow.query.filter(Follow.follower == userId).all()
            following = Follow.query.filter(Follow.follow == userId).all()

            return unicode_safe_json_dumps(
                {
                    "now_follower": [er.follow for er in follower],
                    "now_following": [ing.follower for ing in following]
                }, 200
            )

        else:
            return {"status": "invalid authentication"}, 401

    @swag_from(FOLLOW_POST)
    def patch(self, userId):
        be_followed = request.json['userId']
        user_query = User.query.filter(User.id == userId).first()
        passive_user_query = User.query.filter(User.id == be_followed).first()

        if userId and not user_query:
            return {"status": "invalid authentication"}, 401
        elif userId and user_query and not passive_user_query:
            return {"status": "invalid passive user info"}, 400
        elif userId and user_query and passive_user_query:
            be_followed_set = Follow(follow=userId, follower=be_followed)
            db.session.add(be_followed_set)

            user_query.follow_num += 1
            passive_user_query.follower_num += 1

            db.session.commit()
            return {"status": "It was succeed that adding follow info"}, 201

    @swag_from(FOLLOW_DELETE)
    def delete(self, userId):
        be_deleted = request.json['userId']
        user_query = User.query.filter(User.id == userId).first()
        passive_user_query = User.query.filter(User.id == be_deleted).first()
        
        if userId == be_deleted:
            return unicode_safe_json_dumps({"status": "잘못된 요청입니다. 본인 계정을 팔로우 취소할 수 없습니다."}, 403)

        elif userId == Follow.query.filter(Follow.follower == userId).first():
            return unicode_safe_json_dumps({"status": "수행할 수 없는 명령입니다.(피팔로워는 상대방의 팔로우에 관여할 수 없음)"}, 403)

        elif userId and User.query.filter(User.id == userId).first():
            be_deleted_info = Follow.query.filter(Follow.follow == userId, Follow.follower == be_deleted).first()
            db.session.delete(be_deleted_info)

            user_query.follow_num -= 1
            passive_user_query.follower_num -= 1

            db.session.commit()
            return {"status": "It was succeed that deleting follow info"}, 200

        else:
            return {"status": "invalid authentication"}, 401


class Follower(Resource):

    def get(self, userId):
        pass

    def patch(self, userId):
        pass

    def delete(self, userId):
        pass
