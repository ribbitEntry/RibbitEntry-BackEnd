import os

from flask import request, url_for, current_app, send_from_directory
from werkzeug.utils import secure_filename
from flask_restful import Resource


def allowed_file(filename):
    return '.' in filename and \
           filename.rssplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


class GETImages(Resource):

    def get(self, filename):
        send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


class UploadImages(Resource):

    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            go_link = url_for('uploaded_file', filename=filename)
            return go_link
