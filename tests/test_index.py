from flask_testing import TestCase

import exampleapp


class IndexTestCase(TestCase):
    def create_app(self):
        return exampleapp.create_app()

    def test_index_returns_200(self):
        response = self.client.get("/")
        self.assert200(response)
