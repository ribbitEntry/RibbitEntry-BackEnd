from flask_restful import Resource
from flask import request
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.extensions import db
from server.model.comment import Comment
from server.view import unicode_safe_json_dumps
from server.docs.myPage.comment import COMMENT_POST


class PostComment(Resource):

    @swag_from(COMMENT_POST)
    @jwt_required
    def post(self):
        post_num = request.args.get('postId')
        content = request.json['content']

        if content:
            comment = Comment(content=content, user=get_jwt_identity(), post_id=post_num)
            db.session.add(comment)
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글 작성 완료.'}, 201)
        else:
            return unicode_safe_json_dumps({'status': '내용이 없습니다.'}, 400)
