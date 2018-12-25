from flask_restful import Resource
from flasgger import swag_from

from docs.mainpage import MAIN_PAGE_GET


class MainPage(Resource):

    @swag_from(MAIN_PAGE_GET)
    def get(self):
        pass
