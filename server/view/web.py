from flask import render_template, Response
from flask_restful import Resource


class Web(Resource):

    def get(self):
        return Response(render_template('server_docs.html'))
