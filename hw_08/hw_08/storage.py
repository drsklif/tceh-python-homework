# -*- coding: utf-8 -*-

import os
import os.path
import pyqrcode

from hw_08.config import APP_ROOT

__author__ = 'aildyakov'


class Storage(object):
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
        return cls._obj

    @classmethod
    def save(cls, text):
        if text is None:
            return

        try:
            DIR = os.path.join(APP_ROOT, 'qr-codes')
            num = 1 + len([name for name in os.listdir(DIR)
                           if os.path.isfile(os.path.join(DIR, name))])
            qr_name = 'qr-{}.png'.format(num)
            qr = pyqrcode.create(text)
            qr.png(os.path.join(DIR, qr_name), scale=5)
            return qr_name
        except:
            print('Cant save QR-code image')
