from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='2656555s65dfgh5sg15s15sg15sh6s51s65gs51g65s'

posts=[
    {
        'author': 'Felix Silwimba',
        'title': 'Blog post 1',
        'content': 'first blog post',
        'date':'22 April 2019'
    },
    {
        'author': 'Kevin jet',
        'title': 'Blog post 2',
        'content': 'second blog post',
        'date':'23 April 2019'
    }
    ]

@app.route("/")
@app.route("/Home")
def Home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title= 'About')

@app.route("/register")
def register():
    form= RegistrationForm()
    return render_template('register.html', title= 'Register', form= form)    

@app.route("/login")
def login():
    form= LoginForm()
    return render_template('login.html', title= 'Login', form= form) 


if __name__== '__main__':
    app.run(debug=True)