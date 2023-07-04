from flask_wtf import FlaskForm  # Import FlaskForm class from flask_wtf module
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # Import necessary form fields
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError  # Import necessary validators
from flaskweb.models import User  # Import User model from flaskweb.models module


class RegistrationForm(FlaskForm):  # Define a registration form class
    username = StringField('Username',  # Create a StringField for username
                           validators=[DataRequired(), Length(min=2, max=20)])  # Add validators for the field
    email = StringField('Email',  # Create a StringField for email
                        validators=[DataRequired(), Email()])  # Add validators for the field
    password = PasswordField('Password', validators=[DataRequired()])  # Create a PasswordField for password
    confirm_password = PasswordField('Confirm Password',  # Create a PasswordField for confirming password
                                     validators=[DataRequired(), EqualTo('password')])  # Add validators for the field
    submit = SubmitField('Sign Up')  # Create a SubmitField for form submission

    def validate_username(self, username):  # Custom validation method for username field
        user = User.query.filter_by(username=username.data).first()  # Check if the username already exists in the database
        if user:  # If the username is already taken
            raise ValidationError('Username taken. Please choose a different one.')  # Raise a validation error

    def validate_email(self, email):  # Custom validation method for email field
        user = User.query.filter_by(email=email.data).first()  # Check if the email already exists in the database
        if user:  # If the email is already taken
            raise ValidationError('User email taken. Please choose a different one.')  # Raise a validation error


class LoginForm(FlaskForm):  # Define a login form class
    email = StringField('Email',  # Create a StringField for email
                        validators=[DataRequired(), Email()])  # Add validators for the field
    password = PasswordField('Password', validators=[DataRequired()])  # Create a PasswordField for password
    remember = BooleanField('Remember Me')  # Create a BooleanField for remember me option
    submit = SubmitField('Login')  # Create a SubmitField for form submission
