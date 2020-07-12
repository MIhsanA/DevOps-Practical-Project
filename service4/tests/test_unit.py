from flask import url_for
from flask_testing import TestCase
from app import app
class TestBase(TestCase):
    def create_app(self):
        return app
class TestApi2(TestBase):
    def test_white_colour(self):
        response=self.client.post('/colour', data='ihsan')
        self.assertIn(b'white', response.data)

    def test_red_colour(self):
        response=self.client.post('/colour', data='rob')
        self.assertIn(b'red', response.data)

    def test_gray_colour(self):
        response=self.client.post('/colour', data='gemy')
        self.assertIn(b'gray', response.data)


    def test_blue_colour(self):
        response=self.client.post('/colour', data='ben')
        self.assertIn(b'blue', response.data)

    def test_green_colour(self):
        response=self.client.post('/colour', data='niel')
        self.assertIn(b'green', response.data)

    def test_black_colour(self):
        response=self.client.post('/colour', data='osin')
        self.assertIn(b'black', response.data)
