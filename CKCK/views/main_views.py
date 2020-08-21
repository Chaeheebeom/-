from flask import Blueprint, render_template, redirect, url_for, request

from models.Model import Usercontent

from Forms.Form import SearchForm

bp = Blueprint('main' , __name__, url_prefix='/')

@bp.route('/root/')
def root():
    return redirect(url_for('main.main'))

@bp.route('/')
def main():
    return render_template('index.html',main='main')

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

@bp.route('/search/',methods=('GET','POST'))
def search():
    print('dsds')
    if request.method == 'POST':
        subject=request.form['subject']
        content_list=Usercontent.query.filter(Usercontent.content.like("%"+subject+"%")).all()
        return render_template('index.html',content_list=content_list)
