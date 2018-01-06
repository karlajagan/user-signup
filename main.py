from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="Signup")

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    return render_template('hello.html', title="Welcome", name=username)


app.run()