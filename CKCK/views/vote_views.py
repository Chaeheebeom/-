from flask import g, session, Blueprint, render_template, url_for, request, flash,json

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect,secure_filename

from main import db

from datetime import datetime

from sqlalchemy import select,delete

from models.Model import User,Usercontent,Comment,usercontent_like_voter,comment_like_voter

bp = Blueprint('vote' ,__name__, url_prefix='/vote')

@bp.route('/contentlike/<int:usercontent_id>/',methods=('GET','POST'))
def usercontentlike(usercontent_id):
    content=Usercontent.query.get_or_404(usercontent_id)
    content.voter.append(g.user)
    db.session.commit()
    return redirect(url_for('auth.detail',content_id=usercontent_id))

@bp.route('/commentlike/<int:comment_id>/',methods=('GET','POST'))
def commentlike(comment_id):
    comment=Comment.query.get_or_404(comment_id)
    comment.voter.append(g.user)
    db.session.commit()

    return redirect(url_for('auth.detail',content_id=comment.usercontent_id))

@bp.route('/cancle/<int:usercontent_id>/<int:user_id>/')
def cancle(usercontent_id,user_id):
    q=usercontent_like_voter.delete().where(
        usercontent_like_voter.c.usercontent_id == usercontent_id).where(usercontent_like_voter.c.user_id == user_id)
    db.session.execute(q)
    db.session.commit()
    return redirect(url_for('auth.detail',content_id=usercontent_id))

@bp.route('/cancle/<int:comment_id>/<int:user_id>/<int:usercontent_id>/')
def commentcancle(comment_id,user_id,usercontent_id):
    q=comment_like_voter.delete().where(
        comment_like_voter.c.comment_id == comment_id).where(comment_like_voter.c.user_id == user_id)
    db.session.execute(q)
    db.session.commit()
    return redirect(url_for('auth.detail',content_id=usercontent_id))