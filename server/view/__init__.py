import json

from sqlalchemy.orm import sessionmaker
from flask import Flask, Response
from flask_restful import Api

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
        self.api.add_resource(GETImages, '/api/images/<filename>')

        from server.view.user.myPage.images import UploadImages
        self.api.add_resource(UploadImages, '/api/upload-images/<postId>')


def unicode_safe_json_dumps(data, status_code=200):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status_code,
        content_type='application/json; charset=utf8'
    )
