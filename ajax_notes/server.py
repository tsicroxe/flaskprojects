from flask import Flask, render_template, request

from mysqlconnection import MySQLConnector
application = Flask(__name__)

mysql = MySQLConnector(application, 'mydb')

query = mysql.query_db("SELECT * FROM emails")
print query


@application.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', emails=emails)

application.run(debug=True)
