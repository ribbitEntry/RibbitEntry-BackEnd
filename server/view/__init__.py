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
        from view.user.login import Login
        self.api.add_resource(Login, '/api/login')

        from view.user.login.signUp import SignUp
        self.api.add_resource(SignUp, '/api/sign-up')

        from view.web import Web
        self.api.add_resource(Web, '/server-status')

        from view.search import Search
        self.api.add_resource(Search, '/api/search')

        from view.posts.post import Post
        self.api.add_resource(Post, '/api/posts')

        from view.mainPage.MainPage import MainPage
        self.api.add_resource(MainPage, '/api/main-page')

        from view.user.myPage.MyPage import MyPage
        self.api.add_resource(MyPage, '/api/my-page')
