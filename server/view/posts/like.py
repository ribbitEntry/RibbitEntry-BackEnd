from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.model.user import User
from server.model.post import Post


class Like(Resource):
    @swag_from()
    @jwt_required
    def post(self):
        userId = get_jwt_identity()
        postId = request.json['postId']

        user = User.query.filter_by(id=userId).first()
        post = Post.query.filter_by(postId=int(postId)).first()
        
        if user and post:
            
        else:
            return {"status": "invalid user authentication"}, 401