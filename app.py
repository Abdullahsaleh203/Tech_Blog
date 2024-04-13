from flask import Flask ,render_template , url_for ,flash , redirect
from forms import RegistrationForm , LoginForm 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
# import os
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, ForeignKey, Column, String ,Integer, CHAR

app = Flask(__name__)
app.config['SECRET_KEY'] = '6f2ce3abf636b7a22328e3e1162a90cf'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False,defult='default.jpg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}','{self.image_file}')"


# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(app, model_class=Base)

# class User(db.Model):
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)

# with app.app_context():
#     db.create_all()

#     db.session.add(User(username="example"))
#     db.session.commit()

#     users = db.session.execute(db.select(User)).scalars()

posts = [
    {
        "author":"Abdallah",
        "title": "blog post 1",
        "content":"first post content",
        "date_content":"April 5 ,2024"
    },
    {
        "author":"Abdallah",
        "title": "blog post 2",
        "content":"second post content",
        "date_content":"April 5 ,2024"
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts,title ="home")


@app.route('/about')
def about():
    return render_template('about.html',title ="About") 


    
@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form,title ="Register")

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form , title ="Login") 

# @app.route("/dashboard",methods=['GET', 'POST'])
# def dashboard():
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['logged_in'] = True
#         flash('You have been logged in!', 'success')
#         return redirect(url_for('add'))
#     if 'logged_in' in session:
#         return render_template("dashboard.html",title ="Dashboard")
#     else:
#         return redirect(url_for('login'))

# @app.route("/add",methods=['GET', 'POST'])
# def add():
#     if 'logged_in' in session:
#         form = BlogPostForm() 
#         if form.validate_on_submit():
#             flash(f'Post added!', 'success')        
#             return redirect(url_for('home'))
#         blogposts = Blogpost.query()
#         return render_template('add.html')
#     else:
#         return redirect(url_for('login'))

# @app.route("/logout")
# def logout():
#     session.pop('logged_in', None)
#     flash('You have been logged out', 'success')
#     return redirect(url_for('login'))

    #     return redirect(url_for('home'))
    # return render_template('login.html', form=form, title ="Login")



if __name__ == '__main__':
    app.run(debug=True, port=8000)






# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST':

#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = loginForm()
#     if form.validate_on_submit():
