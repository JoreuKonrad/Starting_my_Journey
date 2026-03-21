# Just following a Youtube course channel

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1> Helloo World! </h1>"

@app.route('/user/<name>')

def user(name):
    return "<h1> Hellooo {} </h1>".format(name)


