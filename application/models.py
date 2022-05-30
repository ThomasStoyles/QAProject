from flask import Flask, render_template, request, url_for, redirect
import os
from sqlalchemy import Integer
from application import db
from flask_sqlalchemy import SQLAlchemy
from  wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_wtf import FlaskForm


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dev_name = db.Column(db.String(30))
    games = db.relationship('Games', backref='dev')

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'))

class GameForm(FlaskForm):
    game_name = StringField ('Please enter game title: ')
    age_rating = SelectField ('age rating', choices=[('3','3'), ('5','5'), ('7','7'), ('12','12'), ('15','15'), ('18','18')])
    price = IntegerField ('Please eneter the price: ')
    developer = SelectField ('Please enter developer name: ', choices=[])
    submit = SubmitField('Submit')

class DevForm(FlaskForm):
    dev_name = StringField ('Please eneter developer name: ')
    submit = SubmitField('Submit')



# class CustomerForm(FlaskForm):
#     f_name = StringField ('Please Enter your name: ')
#     l_name = StringField ('Please Enter your name: ')
#     submit = SubmitField ('submit')

