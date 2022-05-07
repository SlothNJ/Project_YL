from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    file = FileField('Обложка', validators=[FileRequired()])
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')