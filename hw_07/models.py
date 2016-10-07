# -*- coding: utf-8 -*-

import json
import datetime

__author__ = 'aildyakov'


class Storage(object):
    items = None
    _obj = None
    db_filename = 'database.json'

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
            try:
                with open(cls.db_filename, 'rt') as db:
                    cls.items = json.load(db)
            except:
                print('Cant load posts from DB')
        return cls._obj

    @classmethod
    def save(cls):
        if cls.items is None:
            return
        try:
            with open(cls.db_filename, 'wt') as db:
                json.dump(cls.items, db, default = lambda o: o.__dict__, indent = 4)
        except:
             print('Unexpected error occured while saving post to DB')


class BlogPostModel(object):
    def __init__(self, form_data, id):
        self.id = id
        self.title = form_data['title']
        self.text = form_data['text']
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        full_name = form_data['author']
        first_space_index = full_name.find(' ')
        if first_space_index == -1:
            raise(Exception('Incorrect name'))
        self.author_name = full_name[0:first_space_index]
        self.author_lastname = full_name[first_space_index+1:len(full_name)]
