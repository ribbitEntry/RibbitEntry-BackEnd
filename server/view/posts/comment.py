from flask_restful import Resource
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.extensions import db
from server.model.comment import Comment
from server.view import unicode_safe_json_dumps


class PostComment(Resource):

    @jwt_required
    def post(self):
        post_num = request.args.get('postId')
        content = request.json['content']

        if content:
            comment = Comment(content=content, user=get_jwt_identity(), post_id=post_num)
            db.session.add(comment)
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글 작성 완료.'}, 200)
        else:
            return unicode_safe_json_dumps({'status': '내용이 없습니다.'}, 400)
