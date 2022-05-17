from distutils.log import debug
import logging
from flask import Flask, render_template, url_for
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
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug = True)