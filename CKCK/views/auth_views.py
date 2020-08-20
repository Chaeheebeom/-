from flask import g, session, Blueprint, render_template, url_for, request, flash,json

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect,secure_filename

from main import db

from Forms.userForms import UserCreateForm, UserLoginForm
from models.Model import User

bp = Blueprint('auth' ,__name__, url_prefix='/')

@bp.route('/signup/',methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.root'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html',form=form)

@bp.route('/signin/', methods=('GET','POST'))
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.root'))
        flash(error)
    return render_template('auth/signin.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/signout/',methods=('GET','POST'))
def signout():
    session.clear()
    return redirect(url_for('main.root'))

@bp.route('/imgupload/',methods=('GET','POST'))
def imgupload():
    user_id = session.get('user_id')

    if request.method == 'POST':
        file = request.files['file']
        file.save("static/img/"+secure_filename(file.filename))
        return redirect(url_for('main.root'))
    return render_template('auth/fileupload.html')