from flask import Flask ,render_template , url_for ,flash , redirect , request
from tech_blog import app ,db , bcrypt, login_manager
from tech_blog.forms import RegistrationForm , LoginForm
from tech_blog.models import User, Post 
from flask_login import login_user, current_user, logout_user, login_required

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

posts = [
    {
        "author":"Abdallah",
        "title": "post 1",
        "content":"first post content",
        "date_content":"April 5 ,2024"
    },
    {
        "author":"Abdallah",
        "title": "post 2",
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form , title ="Login") 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
