from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('почта', validators=[DataRequired()])
    date = DateTimeField('дата доставки', validators=[DataRequired()])
    address = StringField('адрес доставки', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
