# -*- coding: utf-8 -*-

from app import db

__author__ = 'aildyakov'


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), nullable=False, unique=True)
    name = db.Column('name', db.String(150), nullable=False)
    birthday = db.Column('birthday', db.Date, nullable=False)

    def __init__(self, username, name, birthday):
        self.username = username
        self.name = name
        self.birthday = birthday