from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', 
        title="Signup", username = '', username_error = '',
        password = '', password_error ='', 
        val_password = '', validate_error='',
        email='', email_error='')

def is_space(word):
    if ' ' in word:
        return True
    else:
        return False


@app.route("/", methods=['POST']) 
def validate_data():

    username = request.form['username']
    password = request.form['password']
    val_password = request.form['val_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    validate_error = ''
    email_error = ''

    if is_space(username):
        username_error = "Username should not contain spaces"
        username = ""
    # else:
    #     if length(username) <= 3 and length(username) >= 20:
    #         username_error = 

    if is_space(password):
        password_error = "Password should not contain spaces"
        password = ""

    if is_space(val_password):
        validate_error = "Password should not contain spaces"
        val_password = ""

    if email != '':
        if is_space(email):
            email_error = "Email should not contain spaces"
            email = ""        

    # if not username_error and not password_error and \
    #     not validate_error and not email_error:
    #     return "Success!"

    # else:
    return render_template('signup.html', 
        title="Signup", username_error = username_error,
        password_error =password_error, 
        validate_error=validate_error,
        email_error=email_error, username = username,
        password = password, val_password = val_password,
        email = email)   

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    return render_template('hello.html', title="Welcome", name=username)


app.run()