from distutils.log import debug
from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug = True)