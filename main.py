from flask import Flask, request, redirect, render_template
# import cgi
# import os
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
    if field == "" and text != "Email ":
        error = text+"must not be empty"
    elif is_space(field):
        error = text+"should not contain spaces"
        field = ""
    else:
        if len(field) <= 3 or len(field) >= 20:
            error = text+"must have between 3 and 20 characters"
            field = ""
    return error, field   

def validate_email(field):
    error = ""
    ats = False
    count = 0
    count2 = 0
    point = False
    spec = False
    i = 0
    special_char = string.punctuation
    for i in range(len(field)):
        if field[i] in special_char:
            if field[i] == "@":
                if count == 0:
                    ats = True
                    count += 1
                else:
                    error = "Email contains more than one @"
                    return error     
            elif field[i] == ".":
                if count2 == 0:
                    count2 += 1                 
                    letter = string.ascii_letters
                    if field[i] == 0:
                        if field[i+1] not in letter:
                            error = "Email has two special characters together"
                            return error
                    elif field[i] == len(field) - 1:
                        if field[i-1] not in letter:
                            error = "Email has two special characters together"
                            return error     
                    else:
                        if field[1-1] not in letter or \
                            field[i+1] not in letter:    
                            error = "Email has two special characters together"
                            return error
                    if count > 0:
                        point = True
                else:
                    error = "Email contains more than one dot"
                    return error
                
            elif field[i] != "_":
                error = "Email contains invalid characters "
                spec = True
                return error
    if ats == True and point == True and spec == False:
        error = ""
    else:
        error = "Email does not contain needed @ or . "
    return error

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
    
    validate_error, val_password = validate_field(val_password,"Password ")
    
    if val_password != password:
        validate_error = "The passwords are not matching"
        password = ""
        val_password = ""

    if email != '':
        email_error, email = validate_field(email,"Email ")
        if email_error == "":
            email_error = validate_email(email)
            if email_error != "":
                email = ""
            

    if not username_error and not password_error and \
        not validate_error and not email_error:
        password = ""
        val_password = ""
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', 
            title="Sign up", username_error = username_error,
            password_error =password_error, 
            validate_error=validate_error,
            email_error=email_error, username = username,
            password = "", val_password = "",
           # password = password, val_password = val_password,
            email = email)   

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', title="Welcome", name=username)
 
app.run()