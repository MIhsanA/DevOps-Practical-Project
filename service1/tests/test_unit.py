from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase
import requests_mock
from application import app, db, bcrypt
from application.models import Person
from os import getenv 

class TestBase(TestCase):

    def create_app(self):


        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        
        
    

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class Test_Person(TestBase):

    def test_new_name(self):
        with self.client:
            response = self.client.post(
                '/new',
                data=dict(
                    name="ihsan"
                ),
                follow_redirects=True
            )
            self.assertIn(b'ihsan', response.data)

class TestGenerate(TestBase):
    def test_generate(self):
        with requests_mock.mock() as g:
            g.get("http://service2:5001/number", text="3")
            g.get("http://service3:5002/car", text="bmw")
            g.post("http://service4:5003/colour", text="blue")
            response = self.client.post(url_for('/', data = ""))
            self.assertIn(b'3', response.data)
            self.assertIn(b'bmw', response.data)
            self.assertIn(b'blue', response.data)

