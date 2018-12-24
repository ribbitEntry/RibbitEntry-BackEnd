from flask_restful import Resource
from flasgger import swag_from

from docs.myPage import MY_PAGE_GET


class MyPage(Resource):

    @swag_from(MY_PAGE_GET)
    def get(self):
        pass
