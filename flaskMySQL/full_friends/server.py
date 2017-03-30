from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secretkey'
mysql = MySQLConnector(app, 'friends')

@app.route('/', methods=['GET'])
def index():
    query = "SELECT * from friends_table"
    friends = mysql.query_db(query)
    return render_template ('index.html', all_friends = friends)

@app.route('/create')
def create_user():
  return render_template ('create.html')

@app.route('/processnewuser', methods=['POST'])
def process_new_user():
    query = "INSERT INTO friends_table (first_name, last_name, email) VALUES(:fname, :lname, :email)"
    data = {
    'fname': request.form['created_fname'],
    'lname': request.form['created_lname'],
    'email': request.form['created_email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    query = "SELECT * from friends_table WHERE id = :specific_id"
    data = { 'specific_id' : id }
    friends = mysql.query_db(query, data)
    return render_template('edit.html',one_friend = friends[0])

@app.route('/update/<id>', methods=['POST'])
def update(id):
  query = "UPDATE friends_table SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
  data = {
         'first_name': request.form['update_fname'],
         'last_name':  request.form['update_lname'],
         'email': request.form['update_email'],
         'id': id
         }
  mysql.query_db(query, data)
  return redirect('/')

@app.route('/delete/<id>', methods=['GET'])
def delete_user(id):
    query = "DELETE FROM friends_table WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
