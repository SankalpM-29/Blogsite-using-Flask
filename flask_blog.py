from distutils.log import debug
import logging
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '44d5e72e1e885b0fbe6c15c958bdcff6'

posts = [
    {
        'author': 'Sankalp',
        'title': 'Animals',
        'date_posted': 'April 20'
    },
    {
        'author': 'Virat',
        'title': 'Fruits',
        'date_posted': 'April 22'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.in' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug = True)