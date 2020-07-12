from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestApiCall(TestBase):
    def test_number(self):
        response = self.client.get('/number')
        self.assertIn(response.data.decode('utf-8'), ['1','2','3','4','5','6','7','8','9','10'])
