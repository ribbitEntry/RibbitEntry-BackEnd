import os
import json

from flask import Flask, Response, current_app, url_for
from flask_restful import Api
from sqlalchemy.orm import sessionmaker
from werkzeug.utils import secure_filename

Session = sessionmaker()
session = Session()


class Router():
    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def register(self):
        from server.view.user.login.login import Login
        self.api.add_resource(Login, '/api/login')

        from server.view.user.login.signUp import SignUp
        self.api.add_resource(SignUp, '/api/sign-up')

        from server.view.web.web import Web
        self.api.add_resource(Web, '/server-status')

        from server.view.search.search import Search
        self.api.add_resource(Search, '/api/search')

        from server.view.posts.post import Posts
        self.api.add_resource(Posts, '/api/posts')

        from server.view.mainPage.MainPage import MainPage
        self.api.add_resource(MainPage, '/api/main-page')

        from server.view.user.myPage.MyPage import MyPage
        self.api.add_resource(MyPage, '/api/my-page')

        from server.view.follow.following import Following
        self.api.add_resource(Following, '/api/follow')

        from server.view.user.myPage.images import GETImages
        self.api.add_resource(GETImages, '/api/images/<postId>/<fileId>')

        from server.view.color.color import Color
        self.api.add_resource(Color, '/api/color')


def unicode_safe_json_dumps(data, status_code=200):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status_code,
        content_type='application/json; charset=utf8'
    )


def allowed_file(filename):
    return '.' in filename and \
           filename.split('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def upload_files(files, userId, postId):

    url_list = []
    directory = current_app.config['UPLOAD_FOLDER'] + '/' + userId + '/' + postId

    if files and userId:
        os.makedirs(directory)

    for file in files:
        print(file.filename)

        if file and allowed_file(file.filename):
            file_name = secure_filename(file.filename)
            file.save(os.path.join(directory, file_name))

            file_id = postId + '/' + file_name

            from server.view.user.myPage.images import GETImages
            url_list.append((url_for(GETImages, file_id)))

    return url_list
