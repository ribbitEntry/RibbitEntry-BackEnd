from flask_restful import Resource
from flask import request

from server.model.post import Post
from server.model.comment import Comment
from server.view import unicode_safe_json_dumps


class PostCommentView(Resource):

    def get(self):
        post_num = request.args.get('postId')
        post_info = Post.quere.filter(Post.post_id == post_num).first()
        comment = Comment.quere.filter(Comment.post_id == post_num).all().order_by(Post.date)

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
