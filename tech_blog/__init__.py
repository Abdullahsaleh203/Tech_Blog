from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
# from tech_blog.models import User, Post
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '6f2ce3abf636b7a22328e3e1162a90cf'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from tech_blog import routes
