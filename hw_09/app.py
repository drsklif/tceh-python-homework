# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.widgets import TextArea
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy.exc import IntegrityError

import re
import config
import logging

logger = logging.getLogger(__name__)

__author__ = 'aildyakov'

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    from models import Post

    post_form_class = model_form(Post, base_class=FlaskForm, db_session=db.session, exclude=['time_stamp'],
                                 field_args={
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
                                 })

    if request.method == 'POST':
        form = post_form_class(request.form)
        if form.validate():
            try:
                model = Post(**form.data)
                db.session.add(model)
                db.session.commit()
                flash('Your post added!')
                return redirect(url_for('home'))
            except IntegrityError:
                db.session.rollback()
                flash('This post is already exist')
            except Exception as ex:
                logger.error(ex)
                db.session.rollback()
                flash('Cant save post: ' + str(ex))
        else:
            logger.error('Someone have submitted an incorrect form!')
            flash('Invalid form. Please check fields')
    else:
        form = post_form_class()

    return render_template(
        'home.html',
        form=form,
        items=Post.query.all(),
    )


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
