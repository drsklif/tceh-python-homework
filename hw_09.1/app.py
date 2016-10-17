from datetime import  datetime, timedelta
from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy.exc import IntegrityError
from utils import init_db

import config
import logging

logger = logging.getLogger(__name__)

__author__ = 'aildyakov'

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    from models import User

    user_form_class = model_form(User, base_class=FlaskForm, db_session=db.session)

    if request.method == 'POST':
        form = user_form_class(request.form)
        if form.validate():
            try:
                model = User(**form.data)
                db.session.add(model)
                db.session.commit()
                flash('User created!')
                return redirect(url_for('home'))
            except IntegrityError:
                db.session.rollback()
                flash('This user is already exist')
            except Exception as ex:
                logger.error(ex)
                db.session.rollback()
                flash('Cant save user: ' + str(ex))
        else:
            logger.error('Someone have submitted an incorrect form!')
            flash('Invalid form. Please check fields')
    else:
        form = user_form_class()

    age18 = datetime.now() - timedelta(days=365.25 * 18)
    users = User.query.filter(User.birthday < age18)

    return render_template(
        'home.html',
        form=form,
        items=users,
    )

if __name__ == '__main__':
    init_db()
    app.run()
