from unittest import TestCase
from urllib import response
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import DevForm, Developer, Games, GameForm, DevForm
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
            SECERT_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app


    # tests addition function
    def setUp(self):
        db.create_all()
        #adding a game to the db 
        game1 = Games(name='Fallout')
        db.session.add(game1)
        db.session.commit()
        #adding developers
        dev1 = Games(name='Bethesda')
        db.session.add(dev1)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class Testview(TestBase):
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertIn(b'Fallout', response.data)
        self.assertIn(b'Bethesda', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        #Test delete functionality
        response = self.client.post(url_for('delete', name="Fallout", dev="Bethesda"
        self.assertNotIn('Fallout', str(response.data))
        self.assertNotIn('Bethesda', str(response.data))
