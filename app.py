from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import flask.ext.whooshalchemy as whooshalchemy
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Companies(db.Model):
    __searchable__ = ['title', 'content']
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    location = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    description = db.Column(db.String(255))
    rating = db.Column(db.String(255))
    def __init__(self, name, category, location, phone, email, description):
 
        self.name = name
        self.category = category
        self.location = location
        self.phone = phone
        self.email = email
        self.description = description
        #self.rating = rating

    def __repr__(self):
        return '<companies {} {} {} {} {} {}>'.format(
            self.name,
            self.category,
            self.location,
            self.phone,
            self.email,
            self.description )

class Freelancers(db.Model):
    __tablename__ = 'freelancers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    location = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    description = db.Column(db.String(255))
    rating = db.Column(db.String(255))
    def __init__(self, name, category, location, phone, email, description):
 
        self.name = name
        self.category = category
        self.location = location
        self.phone = phone
        self.email = email
        self.description = description
        #self.rating = frating

    def __repr__(self):
        return '<freelancers {} {} {} {} {} {}>'.format(
            self.name,
            self.category,
            self.location,
            self.phone,
            self.email,
            self.description )

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/companies', methods=['GET', 'POST'])
def company():
    companyDetails = Companies.query.all()
    return render_template("company.html", companyDetails = companyDetails)


@app.route('/addCompany', methods=['GET', 'POST'])
def addcompany():
    if request.method == 'POST':
 
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        phone = request.form['phone']
        email = request.form['email']
        description = request.form['description']
 
        my_data = Companies(name, category, location, phone, email, description)
        db.session.add(my_data)
        db.session.commit()
 
        return redirect('/companies')
    return render_template('addcompany.html')

@app.route('/editCompany/<id>', methods = ['GET', 'POST'])
def editcompany(id):
    companyDetails = Companies.query.filter_by(id=id).first_or_404()
    return render_template('updatecompany.html',companyDetails=companyDetails)

@app.route('/updateCompany/<id>', methods = ['GET', 'POST'])
def updatecompany(id):
    if request.method == 'POST':
        my_data = Companies.query.get(id)
        #print(request.form.get('id'))
        #print(request.form['name'])
        my_data.name = request.form['name']
        my_data.category = request.form['category']
        my_data.location = request.form['location']
        my_data.phone = request.form['phone']
        my_data.email = request.form['email']
        my_data.description = request.form['description']
        db.session.commit()
        #flash("Employee Updated Successfully")
        return redirect('/companies')

@app.route('/deleteCompany/<id>', methods = ['GET', 'POST'])
def deletecompany(id):
    my_data = Companies.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect("/companies")

@app.route('/searchCompany',methods=['GET', 'POST'])
def searchcompany():
    results = Companies.query.whoosh_search(request.args.get('name')).all()
    return render_template('company.html', companyDetails=results)

@app.route('/profilesCompany/<id>')
def profilecompany(id):
    companyDetails = Companies.query.filter_by(id=id).first_or_404()
    #freelancersDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('ProfileCompany.html',companyDetails=companyDetails)


@app.route('/freelancers', methods=['GET', 'POST'])
def freelancers():
    freelancersDetails = Freelancers.query.all()
    return render_template("freelancers.html",freelancersDetails = freelancersDetails)

@app.route('/addFreelancers', methods=['GET', 'POST'])
def addfreelancer():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        phone = request.form['phone']
        email = request.form['email']
        description = request.form['description']
 
        my_data = Freelancers(name, category, location, phone, email, description)
        db.session.add(my_data)
        db.session.commit()
 
        return redirect('/freelancers')
    return render_template('addfreelancer.html')

@app.route('/editFreelancer/<id>', methods = ['GET', 'POST'])
def editfreelancer(id):
    freelancerDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('updatefreelancer.html',freelancerDetails=freelancerDetails)

@app.route('/updateFreelancer/<id>', methods = ['GET', 'POST'])
def updatefreelancer(id):
    if request.method == 'POST':
        my_data = Freelancers.query.get(id)
        #print(request.form.get('id'))
        #print(request.form['name'])
        my_data.name = request.form['name']
        my_data.category = request.form['category']
        my_data.location = request.form['location']
        my_data.phone = request.form['phone']
        my_data.email = request.form['email']
        my_data.description = request.form['description']
        db.session.commit()
        #flash("Employee Updated Successfully")
        return redirect('/freelancers')

@app.route('/deleteFreelancer/<id>', methods = ['GET', 'POST'])
def deletefreelancer(id):
    my_data = Freelancers.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect("/freelancers")

@app.route('/profilesFreelancer/<id>')
def profilefreelancer(id):
    freelancersDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('ProfileFreelancer.html',freelancersDetails=freelancersDetails)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/addCase')
def addCase():
    companyDetails = Companies.query.all()
    return render_template('addCase.html', companyDetails = companyDetails)


if __name__ == "__main__":
    app.run(debug=True)