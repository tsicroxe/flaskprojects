#Make a login / registration
#users table, banking table: account id, deposit, withdrawl, balance, confirmation,

from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector

application = Flask(__name__)
mysql = MySQLConnector(application, 'banking')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/login')
def login():
    return render_template('login.html')


@application.route('/registration', methods=["GET", "POST"])
def registration():

    errors = []
    
    if request.method == "GET":
        return render_template('registration.html')
    elif request.method =="POST":
        query = "SELECT * FROM users"
        request.form['first_name'] #You will need to loop through users

application.run(debug=True)
