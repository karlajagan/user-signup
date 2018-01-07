from flask import Flask, request, redirect, render_template
import cgi
import os
import string


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

def validate_field(field,text):
    error = ""
    if field == "":
        error = text+"must not be empty"
    if is_space(field):
        error = text+"should not contain spaces"
        field = ""
    else:
        if len(field) <= 3 and len(field) >= 20:
            error = text+"must have between 3 and 20 characters"
    return error, field        

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

    username_error, username = validate_field(username,"Username ")
    
    password_error, password = validate_field(password,"Password ")
    
    validate_error, val_password = validate_field(val_password,"Password")
    if val_password != password:
        validate_error = "The passwords are not matching"
        password = ""
        val_password = ""


    if email != '':
        if is_space(email):
            email_error = "Email should not contain spaces"
            email = ""        

    if not username_error and not password_error and \
        not validate_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signup.html', 
            title="Signup", username_error = username_error,
            password_error =password_error, 
            validate_error=validate_error,
            email_error=email_error, username = username,
            password = password, val_password = val_password,
            email = email)   

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
 #   return render_template('welcome.html', title="Welcome", name=username)
    return '<h1>Welcome, {0}.'.format(username)

app.run()