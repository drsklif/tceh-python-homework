# -*- coding: utf-8 -*-

from flask import request, render_template, flash, url_for, redirect, Blueprint, jsonify, abort
from app import logger
from models import db
from forms import PostForm, CommentForm

__author__ = 'aildyakov'

blog = Blueprint('blog', __name__, url_prefix='/')


@blog.route('/', methods=['GET', 'POST'])
def home():
    from models import Post

    if request.method == 'POST':
        form = PostForm(request.form)
        if form.validate():
            try:
                model = Post()
                form.populate_obj(model)
                db.session.add(model)
                db.session.commit()
                flash('Your post added!')
                return redirect(url_for('blog.home'))
            except Exception as ex:
                logger.error(ex)
                db.session.rollback()
                flash('Cant save post: ' + str(ex))
        else:
            logger.error('Someone have submitted an incorrect form!')
            flash('Invalid form. Please check fields')
    else:
        form = PostForm()

    return render_template(
        'home.html',
        form=form,
        items=Post.query.all(),
        comments_form=CommentForm()
    )


@blog.route('comment', methods=['GET', 'POST'])
def post_comment():
    from models import Post, Comment

    form = CommentForm(request.form)
    if form.validate():
        model = Comment()
        form.populate_obj(model)
        model.post = Post.query.filter_by(id=model.post_id).first()

        db.session.add(model)
        db.session.commit()

        comment = model.post.comments.order_by(Comment.id.desc()).first()

        return jsonify(comment.serialize)
    else:
        abort(500)
