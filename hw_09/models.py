# -*- coding: utf-8 -*-

from datetime import datetime
from app import db

__author__ = 'aildyakov'


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column('id', db.Integer, primary_key=True)

    title = db.Column(db.String(140), unique=True, nullable=False)

    text = db.Column(db.String(3000), nullable=False)

    time_stamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    author = db.Column('author', db.String(100), nullable=False)

    def __init__(self, title='', text='', time_stamp=None, author=None):
        self.title = title
        self.text = text
        if time_stamp is not None:
            self.time_stamp = time_stamp
        self.author = author
