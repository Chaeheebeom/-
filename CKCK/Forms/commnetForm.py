from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])