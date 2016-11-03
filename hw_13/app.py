# -*- coding: utf-8 -*-

from flask import Flask

import logging

logger = logging.getLogger(__name__)

__author__ = 'aildyakov'


def create_app():
    import config

    app = Flask(__name__)
    app.config.from_object(config)

    from models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from views import blog
    app.register_blueprint(blog)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
