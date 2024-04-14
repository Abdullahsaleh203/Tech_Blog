from flask import Flask ,render_template , url_for ,flash , redirect
from tech_blog import app ,db , bcrypt
from tech_blog.forms import RegistrationForm , LoginForm
from tech_blog.models import User, Post 
from flask_login import login_user

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form,title ="Register")

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(User.email == form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))

        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        #     flash('You have been logged in!', 'success')
        #     return redirect(url_for('home'))
        # else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form , title ="Login") 
