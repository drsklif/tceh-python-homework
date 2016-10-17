# -*- coding: utf-8 -*-

from datetime import datetime
import requests

import logging
logger = logging.getLogger(__name__)

__author__ = 'aildyakov'


def get_new_users(cnt):

    url = 'http://randomuser.ru/api.json'
    resp = requests.get(url, {'results': cnt})

    users = []

    if resp.status_code == 200:
        from models import User
        try:
            resp_json = resp.json()
            for item in map(lambda u: u['user'], resp_json):
                username = item['username']
                name = '{} {} {}'.format(item['name']['last'], item['name']['first'], item['name']['middle'])
                birthday = datetime.fromtimestamp(item['dob'])
                user = User(username, name, birthday)
                users.append(user)
        except Exception as ex:
            print('Error while loading users!')
            logger.error(ex)

    return users


def init_db():
    from app import db
    from models import User
    db.create_all()
    cnt = User.query.count()
    if cnt < 15:
        users = get_new_users(15 - cnt)
        try:
            db.session.add_all(users)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            print('Cant create Users!')
            logger.error(ex)
