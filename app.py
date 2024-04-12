from flask import Flask ,render_template , url_for
from forms import RegistrationForm , LoginForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = '8a519c340ce6193ef0d7900f7dfc6afdd496900e'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home') 
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html') 


    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = loginForm()
#     if form.validate_on_submit():


if __name__ == '__main__':
    app.run(debug=True)
