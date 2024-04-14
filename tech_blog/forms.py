from flask_wtf import FlaskForm 
from wtforms import StringField ,PasswordField ,EmailField ,SubmitField ,BooleanField   
from wtforms.validators import Length ,Email ,EqualTo, DataRequired  ,ValidationError
from email_validator import validate_email, EmailNotValidError 
from tech_blog.models import User 
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=3,max=25)])

#    email = StringField(label='email', 
#                       validators=[DataRequired(),Email()])
    email = EmailField('Email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                                validators=[DataRequired()])
    confirm_password = PasswordField('Conform password',
                                validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        
        user =User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('That username is taken please try another one.')
    def validate_email(self, email):
        email =User.query.filter_by(email= email.data).first()
        if email:
            raise ValidationError('Invalid email address.')
class LoginForm(FlaskForm):

    email = EmailField('email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('password',
                                validators=[DataRequired()])
    remember  = BooleanField('Remember me')
    submit = SubmitField('Login in')
