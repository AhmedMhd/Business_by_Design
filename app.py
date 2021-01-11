from flask import Flask, render_template, request, redirect, url_for, session 
from flask_mysqldb import MySQL 
import MySQLdb.cursors 



app = Flask(__name__) 


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'C2@2020#88&ZOZO'
app.config['MYSQL_DB'] = 'team1db'


mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/company/addcompany')
def addcompany():
    return render_template('addcompany.html')

@app.route('/freelancers')
def freelancers():
    return render_template('freelancers.html')

@app.route('/freelancers/addfreelancers')
def addfreelancers():
    return render_template('addfreelancer.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__": 
	app.run(host ="localhost", port = int("5000")) 