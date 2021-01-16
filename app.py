from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/companies', methods=['GET', 'POST'])
def company():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM companies")
    if resultValue > 0:
        companyDetails = cur.fetchall()
        return render_template('company.html',companyDetails=companyDetails)

@app.route('/companies/addcompany', methods=['GET', 'POST'])
def addcompany():
    if request.method == 'POST':
        # Fetch form data
        companyDetails = request.form
        name = companyDetails['name']
        category = companyDetails['category']
        location = companyDetails['location']
        phone_number = companyDetails['phone_number']
        email = companyDetails['email']
        description = companyDetails['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO companies(name, category, location, phone_number, email, description) VALUES(%s, %s, %s, %s, %s, %s)",(name, category, location, phone_number, email, description))
        mysql.connection.commit()
        cur.close()
        return redirect('/companies')
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