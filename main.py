from flask import Flask , request, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG']  =  True


@app.route('/')
def user_login():
    template = jinja_env.get_template('user-login.html')
    return template.render()


@app.route('/welcome')
def welcome():
    template = jinja_env.get_template('welcome_page.html')
    return template.render(name="Sumit")



@app.route('/validate-form', methods=['POST'])
def validate_form():
    
    username = str.strip(request.form['username'])
    password = str.strip(request.form['password'])
    passwordconfirmation = str.strip(request.form['passwordconfirmation'])
    email = str.strip(request.form['email'])
    
    username_error = ''
    password_error = ''
    passwordconfirmation_error = ''
    email_error = ''

    error = False
    # The user leaves any of the following fields empty: username, password, verify password.then trigger error
    #username or password is not valid if it is less than 3 characters or more than 20 characters

    if username == "" : 
       username_error = "username cant be blank"
       error = True
    elif len(username) <3 or len(username) > 20:
        username_error = "username should be between 3 and 20 characters"
        error = True

    if password == "" : 
       password_error = "password cant be blank"
       error = True
    elif len(password) <3 or len(password) > 20:
        password_error = "password should be between 3 and 20 characters"
        error = True

    if passwordconfirmation == "" : 
       passwordconfirmation_error = "passwordconfirmation cant be blank"
       error = True
    elif len(passwordconfirmation) <3 or len(passwordconfirmation) > 20:
        password_error = "password should be between 3 and 20 characters"
        error = True
    elif password != passwordconfirmation :
        passwordconfirmation_error = "user's password and password-confirmation do not match"
        error = True
    
    #The email field may be left empty, but if there is content in it, 
    # then it must be validated. The criteria for a valid email address are that it has 
    # a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    if email != "" :
        if not (email.count('.') == 1 and email.count('@') == 1 and email.find(' ') == -1 and len(email) > 3 and len(email)<20) :
            email_error = 'Invalid email - It should contain single @, a single ., contains no spaces, and is between 3 and 20 characters long'
            error = True


    if error :
        template = jinja_env.get_template('user-login.html')
        return template.render(
            username = username, 
            username_error = username_error,
            password_error = password_error,
            passwordconfirmation_error = passwordconfirmation_error,
            email = email,
            email_error = email_error)
    else :
        template = jinja_env.get_template('welcome_page.html')
        return template.render(username = username)



app.run()