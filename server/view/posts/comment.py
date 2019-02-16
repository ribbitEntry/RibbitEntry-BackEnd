from flask_restful import Resource
from flask import request
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity, jwt_required

from server.extensions import db
from server.model.comment import Comment
from server.model.post import Post
from server.docs.posts import COMMENT_POST
from server.view import unicode_safe_json_dumps


class PostComment(Resource):

    @swag_from(COMMENT_POST)
    @jwt_required
    def post(self, post_id):
        content = request.json['content']

        if content:
            comment = Comment(content=content, user=get_jwt_identity(), post_id=postId)
            db.session.add(comment)
            db.session.commit()
            return unicode_safe_json_dumps({'status': '글 작성 완료.'}, 201)
        else:
            return unicode_safe_json_dumps({'status': '내용이 없습니다.'}, 400)


class PostCommentView(Resource):

    def get(self):
        post_num = request.args.get('postId')
        post_info = Post.quere.filter(Post.post_id == post_num).first()
        comment = Comment.quere.filter(Comment.post_id == post_num).order_by(Post.date).all()

        post_info = {
            "content": post_info.content,
            "user": post_info.user,
            "image": post_info.image,
            "date": str(post_info.date),
            "like": post_info.like
        }

        if post_num:
            return unicode_safe_json_dumps({
                'post_info': post_info,
                'comment': [
                    {
                        'content': comments.content,
                        'user': comments.user,
                        'date': comments.date
                    } for comments in comment
                ]}, 200)
