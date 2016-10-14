from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

application = Flask(__name__)
mysql = MySQLConnector(application, 'mydb')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
application.secret_key = 'wuzzle'

#Creates dictionary to insert and delete from DB
queries = {
    'create' : "INSERT INTO emails (name, created_at, updated_at) VALUES (:name, NOW(), NOW());",
    'delete' : "DELETE FROM emails WHERE id = :id"
}

#Route that displays our index page
@application.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('index.html')

#Runs the validation route to check email
@application.route('/validate', methods=["POST"])
def validate():
    user_email = request.form['email']
    emails = mysql.query_db("SELECT * FROM emails")
    print emails

    #Checks to see if email already exists
    for email in emails:
        if email['name'] == user_email:
            flash('Email already exists')
            print "This is a duplicate email"
            return redirect('/')

    #Uses regex to check if email is valid and then adds to database
    if(validateEmail(request.form['email'])):
        query = queries['create']
        data = { 'name' : request.form['email'] }
        mysql.query_db(query, data)
        print 'works up utnil this point'
        return redirect('/success')

    #If not a valid address, flashes that it is not a.. valid address.
    else:
        flash("Not a valid address")
        print "Not a valid address"

    return render_template('index.html')

#Route to delete emails
@application.route('/delete/<id>', methods=["POST"])
def delete(id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/success')

#route to display emails
@application.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('index.html', emails=emails)

#Function that uses REGEX to validate email
def validateEmail(email):
    return EMAIL_REGEX.match(email)

application.run(debug=True)
