from flask import Flask ,render_template , url_for ,flash , redirect
from tech_blog import app ,db , bcrypt
from tech_blog.forms import RegistrationForm , LoginForm
from tech_blog.models import User, Post

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
