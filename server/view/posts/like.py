from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from server.model.post import Post
from server.docs.like import LIKE_PATCH
from server.view import session


class Like(Resource):
    @swag_from(LIKE_PATCH)
    @jwt_required
    def patch(self, postId):
        post = Post.query.filter(Post.post_id == int(postId)).first()

        if post:
            post.like += 1
            session.commit()

            return {"like": post.like}, 200
        else:
            return {"status": "invalid user authentication"}, 401
