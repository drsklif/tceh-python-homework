# -*- coding: utf-8 -*-

import re

from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

__author__ = 'aildyakov'


class BlogPostForm(FlaskForm):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=140),
    ])
    text = StringField(label='Article Text', validators=[
        validators.Length(min=10, max=3500),
    ])
    author = StringField(label='Article Author', validators=[
        validators.Regexp(re.compile(r'\w+\s\w+[\s\w]+', re.U), message="Type Author with format 'firstname lastname'"),
        validators.Length(min=3, max=100),
    ])
