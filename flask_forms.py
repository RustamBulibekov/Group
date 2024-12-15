from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField('username')
    email = EmailField('email')
    password = PasswordField('password')
    submit = SubmitField('sign in')
