from flask import g, session, Blueprint, render_template, url_for, request, flash,json

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect,secure_filename

from main import db

from datetime import datetime

from models.Model import User,Usercontent,Comment

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