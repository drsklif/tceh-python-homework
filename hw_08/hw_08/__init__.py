# -*- coding: utf-8 -*-

from flask import Flask
from hw_08 import config

__author__ = 'aildyakov'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

from hw_08 import views
