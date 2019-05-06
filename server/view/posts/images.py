from flask import request, current_app, send_from_directory
from flask_restful import Resource
from flasgger import swag_from

from server.model.post import Post
from docs import IMAGES_GET


class GETImages(Resource):

    @swag_from(IMAGES_GET)
    def get(self):

        args = request.args

        if args.get('postId') and args.get('fileId'):
            userId = Post.query.filter(Post.post_id == args.get('postId')).first().user
            folder = current_app.config['UPLOAD_FOLDER_PATH'] + '/' + str(userId) + '/' + args.get('postId')
            file_name = args.get('fileId')

        elif args.get('profile'):
            folder = current_app.config['UPLOAD_FOLDER_PATH'] + '/' + str(args.get('userId')) + '/profile'
            file_name = args.get('profile')

        elif args.get('background'):
            folder = current_app.config['UPLOAD_FOLDER_PATH'] + '/' + str(args.get('userId')) + '/background'
            file_name = args.get('background')

        return send_from_directory(folder, file_name)
