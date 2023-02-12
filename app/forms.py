from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField(
        label='Username', 
        validators=[DataRequired()]
        )
    email = EmailField(
        label='Email', 
        validators=[DataRequired()]
        )
    password = PasswordField(
        label='Password', 
        validators=[DataRequired()]
        )
    password_repeat = PasswordField(
        label='Repeat Password', 
        validators=[DataRequired(), EqualTo('password', message="Passwords do not match. Please retry.")]
        )
    submit = SubmitField(
        label='Register'
        )

    def validate_username(self, username: str) -> bool:
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("That username is already in use.")
        
    def validate_email(self, email: str) -> bool:
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("That emamil address is already in use.")
