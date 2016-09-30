# -*- coding: utf-8 -*-

import pickle

"""
Storage items
"""

__author__ = 'aildyakov'


class MarkItem(object):
    """Запись журнала с оценками"""
    def __init__(self, name, class_name, mark, lesson):
        self.name = name
        self.class_name = class_name
        self.mark = mark
        self.lesson = lesson

    def __str__(self):
        return 'class: {}; name: {}; lesson: {}; mark: {}.'.format(self.class_name, self.name, self.lesson, self.mark)


class SchoolLog(object):
    """Журнал оценок"""
    obj = None
    marks = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.marks = []
            try:
                with open('school_log.dat', 'rb') as stor:
                    cls.marks = pickle.load(stor)
            except Exception:
                pass
        return cls.obj

    @classmethod
    def add_mark(cls, mark):
        cls.marks.append(mark)

    @classmethod
    def get_all_marks(cls):
        return cls.marks

    @classmethod
    def get_marks_by_name_and_class(cls, name, class_name):
        return [mark for mark in cls.marks if mark.name == name and mark.class_name == class_name]

    @classmethod
    def save(cls):
        with open('school_log.dat', 'wb') as stor:
            pickle.dump(cls.marks, stor, protocol=2)
