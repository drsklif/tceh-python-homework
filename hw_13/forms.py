from flask_wtf import Form
from wtforms import validators
from wtforms.widgets import TextArea, HiddenInput
from wtforms_alchemy import model_form_factory

from models import db, Post, Comment

import re

__author__ = 'aildyakov'


BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class PostForm(ModelForm):
    class Meta:
        model = Post
        only = ['title', 'text', 'author']
        field_args = {
            'title': {
                'validators': [validators.Length(min=4, max=140)]
            },
            'text': {
                'widget': TextArea(),
                'validators': [validators.Length(min=10, max=3000)],
            },
            'author': {
                'validators': [validators.Length(min=3, max=100),
                               validators.Regexp(re.compile(r'\w+\s\w+[\s\w]+', re.U),
                                message="Type Author with format 'firstname lastname'")]
            },
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        only = ['post_id', 'text', 'author']
        field_args = {
            'post_id': {
                'widget': HiddenInput()
            },
            'text': {
                'widget': TextArea(),
                'validators': [validators.Length(min=10, max=3000)],
            },
            'author': {
                'validators': [validators.Length(min=3, max=100),
                               validators.Regexp(re.compile(r'\w+\s\w+[\s\w]+', re.U),
                                                 message="Type Author with format 'firstname lastname'")]
            },
        }
