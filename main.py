from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
#    if request.method = 'POST':

    return render_template('signup.html', title="Signup")

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['username']
    return render_template('hello.html', title="Welcome", name=username)


app.run()