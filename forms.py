from flask_wtf import FlaskForm 
from wtforms import StringField ,PasswordField ,EmailField ,SubmitField ,BooleanField   
from wtforms.validators import Length ,Email ,EqualTo, DataRequired 
from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=6,max=25)])

#    email = StringField(label='email', 
#                       validators=[DataRequired(),Email()])
    email = EmailField('Email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                                validators=[DataRequired()])
    confirm_password = PasswordField('Conform password',
                                validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):

    email = EmailField('email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('password',
                                validators=[DataRequired()])
    remember  = BooleanField('Remember me')
    submit = SubmitField('Login in')
