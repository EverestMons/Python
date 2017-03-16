from flask import Flask, request, render_template, flash, redirect, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key="secret_key"
bcrypt = Bcrypt(app)
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'Login_reg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['login_email']
    password = request.form['login_password']
    query = "SELECT * FROM users WHERE email = :email"
    data = { 'email': email }
    users = mysql.query_db(query, data)
    # session['fname'] = users[0]['first_name']

    is_valid = True

    if len(email) < 1:
        flash("Please specify email")
        is_valid = False

    if len(users) > 1:
        flash('email already registered')
        is_valid = False
    if len(users) is 0:
        flash('user not in database')
        is_valid = False
    if email_regex.search(email) is None:
        flash('invalid email address')
        is_valid = False

    if is_valid:
         if bcrypt.check_password_hash(users[0]['pw_hash'], password):
             return redirect ('/success')
    else:
      return redirect ('/login')




@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/success')
def success():
    query = "select * from users"
    users = mysql.query_db(query)
    return render_template('success.html', all_users = users)

@app.route('/newuser')
def newuser():
    return render_template ('newuser.html')

@app.route('/process', methods=['POST'])
def process_new_user():
    is_valid = True

    fname = request.form['newuser_fname']
    lname = request.form['newuser_lname']
    email = request.form['newuser_email']
    password = request.form['newuser_p']
    password_confirm = request.form['newuser_cp']

    session['fname'] = fname

    if len(fname) < 3:
        flash("First name msut be at least 3 letters long")
        is_valid = False
    if len(lname) < 3:
        flash("Last name msut be at least 3 letters long")
        is_valid = False
    if email_regex.search(email) is None:
        flash('invalid email address')
        is_valid = False
    if len(password) < 8:
        flash("Password must be at least eight characters")
        is_valid = False
    if password  != password_confirm:
        flash("Passwords must match")
        is_valid = False

    if is_valid:

        pw_hash = bcrypt.generate_password_hash(password)
        print pw_hash

        data = {
        'fname' : fname,
        'lname' : lname,
        'email' : email,
        'pw_hash' : pw_hash
        }

        query = "INSERT INTO users(first_name, last_name, email, pw_hash) VALUES(:fname, :lname, :email, :pw_hash)"
        user = mysql.query_db(query, data)
        return redirect('/success')
    else:
        return redirect('/newuser')

app.run(debug=True)
