from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    date = DateField("Date and Time", validators=[DataRequired()])
    submit = SubmitField("Okay, BOOMER")
