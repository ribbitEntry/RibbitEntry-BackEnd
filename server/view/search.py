from flask_restful import Resource
from flasgger import swag_from

from docs.search import SEARCH_GET, SEARCH_POST


class Search(Resource):

    @swag_from(SEARCH_POST)
    def post(self):
        pass

    @swag_from(SEARCH_GET)
    def get(self):
        pass
