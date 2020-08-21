from datetime import datetime

from flask import Blueprint,request ,render_template, redirect, url_for, g

from main import db

from models.Model import Usercontent,Comment

from Forms.commnetForm import CommentForm

bp = Blueprint('comment' ,__name__, url_prefix='/comment')

@bp.route('/create/<int:usercontent_id>/', methods=('GET','POST'))
def create_comment(usercontent_id):
    form = CommentForm()
    usercontent=Usercontent.query.get_or_404(usercontent_id)
    if request.method=='POST' and form.validate_on_submit():
        comment=Comment(user=g.user, content=form.content.data,create_date=datetime.now(),usercontent=usercontent)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('auth.detail',content_id=usercontent_id))
    return render_template('comment/comment_form.html',form=form)

@bp.route('/modify/<int:comment_id>/',methods = ('GET','POST'))
def modify_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if request.method == 'POST':
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('auth.detail',content_id=comment.usercontent_id))
    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form)

@bp.route('/delete/<int:comment_id>/',methods=('GET','POST'))
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('auth.detail', content_id=comment.usercontent_id))