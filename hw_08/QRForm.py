# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextArea

__author__ = 'aildyakov'


class QRForm(FlaskForm):
    text = StringField(label='введите текст для кодирования:', validators=[
        validators.Length(min=5, max=140),
    ], widget=TextArea())
