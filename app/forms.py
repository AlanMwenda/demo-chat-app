from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 30)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 30), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 30)])
    confirm_password = PasswordField('Password', validators=[DataRequired(), Length(1, 30), EqualTo('password')])
    submit = SubmitField('Register')


class PostForm(FlaskForm):
    post = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Submit')    