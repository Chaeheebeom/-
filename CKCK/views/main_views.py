from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('main' ,__name__, url_prefix='/')

@bp.route('/root/')
def root():
    return redirect(url_for('main.index'))

@bp.route('/index/')
def index():
    imgs= getImages()
    maxLen=len(imgs)
    for index in range(maxLen):
        imgs[index]=imgs[index].replace('static/img\\','img/')
    return render_template('index.html',img_list=imgs)

def getImages():
    import glob
    ret = glob.glob('static/img/*.jpg')
    return ret