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
            DEBUG=True, 
            WTF_CSRF_ENABLED=False
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

class TestViewall(TestBase):
    def test_home_get(self):
        #Test home page functionality
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fallout', response.data)
        self.assertIn(b'Bethesda', response.data)


class Testaddgame(TestBase):
    def test_add_game(self):
        #Test game addition 
        response = self.client.post(url_for('add_game'),
        data =dict(game_name="Fallout", age_rating=3, price=5, developer=1),follow_redirects=True
        )
        self.assertIn(b'Fallout', response.data)
        self.assertIn(b'3', response.data )
        self.assertIn(b'5', response.data )
        self.assertIn(b'1', response.data )

class Testadddev(TestBase):
    def test_add_dev(self):
        #Test game addition 
        response = self.client.post(url_for('add_developer'),
        data =dict(dev_name="Bethesda"),follow_redirects=True
        )
        self.assertIn(b'Bethesda', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        #Test delete functionality
        response = self.client.get(url_for('delete', id=1))
        self.assertNotIn(b'Fallout', response.data)
        self.assertNotIn(b'Bethesda', response.data)


class Testupdategame(TestBase):
    def test_update_game(self):
        #Test game addition 
        response = self.client.post(url_for('update', id=1),
        data =dict(game_name="hbvka", age_rating=3, price=8, developer=1),follow_redirects=True
        )
        self.assertIn(b'hbvka', response.data)
        self.assertIn(b'3', response.data )
        self.assertIn(b'1', response.data )
