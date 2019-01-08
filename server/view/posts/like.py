from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.model.user import User
from server.model.post import Post
from server.docs.posts.like import LIKE_PATCH
from server.extensions import db


class Like(Resource):
    @swag_from(LIKE_PATCH)
    @jwt_required
    def patch(self, postId):
        valid_user = User.query.filter(User.id == get_jwt_identity()).first()
        post = Post.query.filter(Post.post_id == int(postId)).first()

        if valid_user and post:
            post.like += 1
            db.session.commit()
            return {"like": post.like}, 200

        elif not valid_user:
            return {"status": "invalid user authentication"}, 401

        elif valid_user and not post:
            return {"status": "post hasn't found."}, 404
