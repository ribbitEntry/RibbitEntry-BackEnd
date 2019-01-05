from functools import wraps

from flask import Response
from unittest import TestCase

from server import create_app
from server.extensions import db


class TCBase(TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.db = db
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def save_url_request(self, url: str = 'https://github.com/by09115') -> Response:
        rv = self.client.post('/', json={'url': url})
        return rv

    def get_url_request(self, key: str) -> Response:
        rv = self.client.get('/' + key)
        return rv


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper()
    return decorator()
