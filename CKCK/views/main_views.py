from flask import Blueprint, render_template, redirect, url_for

from models.Model import Usercontent

bp = Blueprint('main' ,__name__, url_prefix='/')

@bp.route('/root/')
def root():
    return redirect(url_for('main.index'))

@bp.route('/index/')
def index():
    #imgs= getImages()
    #maxLen=len(imgs)
    #for index in range(maxLen):
    #    imgs[index]=imgs[index].replace('static/img\\','img/')
    content_list=Usercontent.query.all()
    return render_template('index.html',content_list=content_list)

@bp.route('/detail/<int:content_id>')
def detail(content_id):
    content = Usercontent.query.filter_by(id=content_id).first()
    return render_template('client/detail.html', content=content)

#def getImages():
#    import glob
#    ret = glob.glob('static/img/*.jpg')
#    return ret