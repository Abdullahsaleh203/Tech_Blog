from datetime import datetime
from tech_blog import db ,login_manager
from sqlalchemy import ForeignKey, Column, String ,Integer, CHAR
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))
class User(db.Model,UserMixin):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        image_file (str): The file path of the user's profile image.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        posts (relationship): The relationship between the user and their posts.

    Methods:
        __repr__(): Returns a string representation of the User object.

    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    # content = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


