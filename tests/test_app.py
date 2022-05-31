from unittest import TestCase
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
    def stop(self):
        db.session.remove()
        db.drop_all()

