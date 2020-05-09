from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Почта', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    date = StringField('Дата и время', validators=[DataRequired()])
    submit = SubmitField('Заказать')
