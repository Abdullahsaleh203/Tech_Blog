from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,EmailField ,SubmitField ,BooleanField 
from wtforms.validators import Length ,Email ,EqualTo, DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(),Length(min=2,max=20)])

#    email = StringField(label='email', 
#                       validators=[DataRequired(),Email()])
    email = EmailField('email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('password',
                                validators=[DataRequired()])
    confirm_password = PasswordField('conforim_password',
                                validators=[DataRequired(),EqualTo('password')])
    sumit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):

    email = EmailField('email', 
                        validators=[DataRequired(),Email()])
    password = PasswordField('password',
                                validators=[DataRequired()])
    remember  = BooleanField('Remember me')
    sumit = SubmitField('Login in')
