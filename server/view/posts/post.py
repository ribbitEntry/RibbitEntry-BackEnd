from flask_restful import Resource
from flasgger import swag_from
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.docs.posts import POST_POST, POST_DELETE
from server.extensions import db
from server.model.post import Post
from server.view import unicode_safe_json_dumps


class Posts(Resource):

    @swag_from(POST_POST)
    @jwt_required
    def post(self):
        content = request.json['content']
        image = request.form['image']

        if content:
            post = Post(content=content, image=image, user=get_jwt_identity())
            db.session.add(post)
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글 작성 완료'}, 201)
        else:
            return unicode_safe_json_dumps({'status': '내용을 작성해주세요'}, 400)

    @swag_from(POST_DELETE)
    @jwt_required
    def delete(self):
        post_id = request.json['post_id']

        if Post.query.filter(Post.post_id == post_id):
            Post.query.filter(Post.post_id == post_id).delete()
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글이 삭제되었습니다.'}, 200)
        else:
            unicode_safe_json_dumps({'status': '없는 글입니다.'}, 400)
