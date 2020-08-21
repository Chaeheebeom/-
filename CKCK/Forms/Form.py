from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SearchForm(FlaskForm):
    subject = TextAreaField('내용', validators=[DataRequired()])