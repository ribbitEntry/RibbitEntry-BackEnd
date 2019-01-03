from flask import current_app, send_from_directory
from flask_restful import Resource


class GETImages(Resource):

    def get(self, postId, fileId):
        folder = current_app.config['UPLOAD_FOLDER'] + '/' + postId
        send_from_directory(folder, fileId)
