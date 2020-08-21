from main import db

#좋아요기능을 위한 모델
#글에 좋아요
usercontent_like_voter = db.Table(
    'usercontent_like_voter',
    db.Column('usercontent_id',db.Integer,db.ForeignKey('usercontent.id',ondelete='CASCADE'),primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
)
#댓글에 좋아요
comment_like_voter = db.Table(
    'comment_like_voter',
    db.Column('comment_id',db.Integer,db.ForeignKey('comment.id',ondelete='CASCADE'),primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

#글내용을 저장하기 위한 것
class Usercontent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey('user.username', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('usercontent_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    filename = db.Column(db.String(200), nullable=False)
    voter = db.relationship('User',secondary=usercontent_like_voter,backref=db.backref('usercontent_voter_set'))

#댓글을 위한 모델
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'),nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    usercontent_id = db.Column(db.Integer,db.ForeignKey('usercontent.id',ondelete='CASCADE'),nullable=True)
    usercontent = db.relationship('Usercontent',backref=db.backref('comment_set'))
    voter = db.relationship('User',secondary=comment_like_voter,backref=db.backref('comment_voter_set'))

