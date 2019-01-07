from flask_restful import Resource
from flask import request
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.docs.color import COLOR_POST
from server.extensions import db
from server.model.user import User
from server.view import unicode_safe_json_dumps


class Color(Resource):

    @swag_from(COLOR_POST)
    @jwt_required
    def post(self):
        color = request.json['color']
        user_id = get_jwt_identity()

        if color:
            user = User.query.filter(User.id == user_id).first()
            user.theme_color = color
            db.session.commit()
            return {'color': User.theme_color}, 200
        else:
            return unicode_safe_json_dumps({'status': 'JWT 인증에 실패하였거나 색상코드가 없습니다.'}, 400)
