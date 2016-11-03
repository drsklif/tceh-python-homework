# -*- coding: utf-8 -*-

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__author__ = 'aildyakov'

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


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


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column('id', db.Integer, primary_key=True)

    time_stamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    author = db.Column('author', db.String(100), nullable=False)

    text = db.Column(db.String(3000), nullable=False)

    post_id = db.Column(db.ForeignKey('post.id'))
    post = db.relationship('Post', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, author=None, text=None, post=None):
        self.author = author
        self.text = text
        self.post = post

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'time_stamp': dump_datetime(self.time_stamp),
            'author': self.author,
            'text': self.text,
            'post_id': self.post_id
        }
