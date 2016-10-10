# -*- coding: utf-8 -*-

from flask import request, render_template, send_from_directory, url_for
from hw_08 import app
import logging

from hw_08.QRForm import QRForm
from hw_08.storage import Storage

logger = logging.getLogger(__name__)

__author__ = 'aildyakov'


@app.route('/', methods=['GET', 'POST'])
def index():
    qr_name = None
    if request.method == 'POST':
        form = QRForm(request.form)
        if form.validate():
            qr_name = url_for('qr', path=Storage.save(form.text.data),
                              _external=True)
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = QRForm()

    return render_template(
        'index.html',
        form=form,
        qr_name=qr_name,
        html_blog='<img src="{}" width="164" height="164"'
                  ' border="0" title="QR код">'.format(qr_name)
    )


@app.route('/qr-codes/<path:path>')
def qr(path):
    return send_from_directory('qr-codes', path)
