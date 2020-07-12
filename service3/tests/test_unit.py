from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestApi2(TestBase):
    def test_car(self):
        response=self.client.get('/car')
        self.assertIn(response.data.decode('utf-8'), ['bmw', 'volvo', 'tesla', 'jeep', 'honda', 'toyota', 'mazda', 'volkswagen', 'kia', 'mercedes'])

