from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from flask_login import LoginManager, current_user

#Create form to enter details in registration-with validators to ensure that data is entered in the right formats
class RegistrationForm(FlaskForm):
    username = StringField('Username',
            validators=[
                DataRequired()
        ]
    )
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
#Check if the email is already in the email column of the user database
        if user:
            raise ValidationError('Email is already in use!')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
#Check if username is already being used
        if user:
            raise ValidationError('Username is already in use!')
#Create login form
class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#Create pokemon form
class PokemonForm(FlaskForm):
    pokemon_name = StringField('Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ]
    )

    pokemon_fast = StringField('fast',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ]
    )

    pokemon_charge = StringField('charge',
        validators=[
            DataRequired(),
            Length(min=4, max=100)
        ]
    )
    #user_id = current_user

    submit = SubmitField('Create Pokemon')

#Create account update form
class UpdateAccountForm(FlaskForm):
        username= StringField('User Name',
                validators=[
                        DataRequired(),
                        Length(min=4, max=30)
                ]
	)

        email =StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )
        submit = SubmitField('Update')

        def validate_email(self,email):
                if email.data != current_user.email:
                        user = User.query.filter_by(email=email.data).first()
                        if user:
                                raise ValidationError('Email already is use - Please choose another')
