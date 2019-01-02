from flask_restful import Resource
from flasgger import swag_from
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.docs.posts import POST_POST, POST_DELETE
from server.extensions import db
from server.model.post import Post


class Posts(Resource):

    @swag_from(POST_POST)
    @jwt_required
    def post(self):
        title = request.json['title']
        content = request.json['content']
        image = request.json['image']

        if title and content:
            post = Post(title=title, content=content, image=image, user=get_jwt_identity())
            db.session.add(post)
            db.session.commit()
            return {'status': '글 작성 완료'}, 201
        else:
            return '제목과 글 모두 작성해주세요', 400

        


    @swag_from(POST_DELETE)
    def delete(self):
        post_id = request.json['post_id']

        db.session.delete(post_id)
        db.session.commit()
