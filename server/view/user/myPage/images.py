from flask import request, current_app, send_from_directory
from flask_restful import Resource

from server.model.post import Post


class GETImages(Resource):

    def get(self):
        args = request.args
        userId = Post.query.filter(Post.post_id == args.get('postId')).first().user
        folder = current_app.config['UPLOAD_FOLDER'] + '/' + str(userId) + '/' + args.get('postId')
        return send_from_directory(folder, args.get('fileId'))
