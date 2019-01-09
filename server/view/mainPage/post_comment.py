from flask_restful import Resource
from flask import request, jsonify

from server.model.post import Post
from server.model.comment import Comment


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
            return jsonify({
                'post_info': post_info,
                'comment': [
                    {
                        'content': comments.content,
                        'user': comments.user,
                        'date': comments.date
                    } for comments in comment
                ]}, 200)
