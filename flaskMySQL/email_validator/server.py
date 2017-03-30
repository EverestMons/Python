from flask import Flask, flash, render_template, redirect, request
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key="secretkey"
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'users')

@app.route('/')
def index ():
    # users = mysql.query_db("SELECT * FROM users")
    # query = "SELECT * FROM users"
    # users = mysql.query_db(query)
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def create():
    query = "INSERT INTO emails (name, email,created_at, updated_at) VALUES (:name, :email, NOW(), NOW())"
    data = {
        'name': request.form['html_name'],
        'email': request.form['html_email']
    }
    mysql.query_db(query, data)
    if not email_regex.match(request.form['html_email']):
        flash("invalid email")
        return redirect('/')
    elif len(request.form['html_name']) < 1:
        flash("'name' is a required field")
        return redirect('/')
    else:
        return redirect ('/success')

@app.route('/success')
def success():
    query = "SELECT * from emails"
    people = mysql.query_db(query)
    return render_template ('success.html', all_people = people)

@app.route('/delete')
def delete():
    return render_template ('delete.html')

@app.route('/processdelete', methods = ['POST'])
def processdelete():
    query = "DELETE FROM emails WHERE email = :email"
    data = {
    'email': request.form['delete_email']
    }
    mysql.query_db(query, data)
    return redirect ('/')

app.run(debug=True)
