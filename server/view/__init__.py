from sqlalchemy.orm import sessionmaker
from flask import Flask
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

        from server.view.posts.post import Post
        self.api.add_resource(Post, '/api/posts')

        from server.view.mainPage.MainPage import MainPage
        self.api.add_resource(MainPage, '/api/main-page')

        from server.view.user.myPage.MyPage import MyPage
        self.api.add_resource(MyPage, '/api/my-page')

        from server.view.follow.following import Follow
        self.api.add_resource(Follow, '/api/follow')
