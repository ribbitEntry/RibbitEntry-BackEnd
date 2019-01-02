from flask_restful import Resource
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.extensions import db
from server.model.user import User
from server.view import unicode_safe_json_dumps


class Color(Resource):

    @jwt_required
    def post(self):
        color = request.json['color']
        user_id = get_jwt_identity()

        if color:
            user = User.query.filter(User.id == user_id).first()
            user.theme_color = color
            db.session.commit()
            return unicode_safe_json_dumps({'status': '테마색을 변경하였습니다.'}, 200)
        else:
            return unicode_safe_json_dumps({'status': '컬러가 없습니다.'}, 400)
