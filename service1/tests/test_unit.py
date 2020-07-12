from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

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

        update=Person(name='ihsan')
        db.session.add(update)
        db.session.commit

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class Person(TestBase):

    def new_name(self):
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
    def test_generat(self):
        with patch('requests.get') as g:
            g.return_value.text = "3"
            with patch('requests.get') as p:
                p.return_value.text = "bmw"
                with patch('request.post') as l:
                    l.return_value.text = "red"
                    response = self.clint.get('/genrate')
                    self.assertin(b'3', response.data)
