from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
 
#Creating model table for our CRUD database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

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
    def __init__(self, name, category, location, phone, email, rating, description):
 
        self.name = name
        self.category = category
        self.location = location
        self.phone = phone
        self.email = email
        self.rating = rating
        self.description = description
        

    def __repr__(self):
        return '<companies {} {} {} {} {} {} {}>'.format(
            self.name,
            self.category,
            self.location,
            self.phone,
            self.email,
            self.rating,
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
    def __init__(self, name, category, location, phone, email, rating, description):
 
        self.name = name
        self.category = category
        self.location = location
        self.phone = phone
        self.email = email
        self.rating = rating
        self.description = description
        

    def __repr__(self):
        return '<freelancers {} {} {} {} {} {} {}>'.format(
            self.name,
            self.category,
            self.location,
            self.phone,
            self.email,
            self.rating,
            self.description )

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect ('/dashboard')
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def index():
    return render_template('dashboard.html')

@app.route('/companies', methods=['GET', 'POST'])
@login_required
def company():
    if request.method == 'POST' :
        name= request.form['name']
        companyDetails = Companies.query.filter(Companies.name.like(name)).all()
        return render_template("company.html", companyDetails = companyDetails)
    companyDetails = Companies.query.all()
    return render_template("company.html", companyDetails = companyDetails)

# query = SPInfo.query
# if stratum:
#     query = query.filter(SPInfo.Stratum == stratum)
# if origin:
#     query = query.filter(SPInfo.Origin == origin)
# if elev:
#     query = query.filter(SPInfo.Elevation.contains(elev))

# results = query.all()

@app.route('/addCompany', methods=['GET', 'POST'])
@login_required
def addcompany():
    if request.method == 'POST':
 
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        phone = request.form['phone']
        email = request.form['email']
        rating = request.form['rating']
        description = request.form['description']
 
        my_data = Companies(name, category, location, phone, email, rating, description)
        db.session.add(my_data)
        db.session.commit()
 
        return redirect('/companies')
    return render_template('addcompany.html')

@app.route('/editCompany/<id>', methods = ['GET', 'POST'])
@login_required
def editcompany(id):
    companyDetails = Companies.query.filter_by(id=id).first_or_404()
    return render_template('updatecompany.html',companyDetails=companyDetails)

@app.route('/updateCompany/<id>', methods = ['GET', 'POST'])
@login_required
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
        my_data.rating = request.form['rating']
        my_data.description = request.form['description']
        db.session.commit()
        #flash("Employee Updated Successfully")
        return redirect('/companies')

@app.route('/deleteCompany/<id>', methods = ['GET', 'POST'])
@login_required
def deletecompany(id):
    my_data = Companies.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect("/companies")

@app.route('/searchCompany',methods=['GET', 'POST'])
@login_required
def searchcompany():
    results = Companies.query.whoosh_search(request.args.get('name')).all()
    return render_template('company.html', companyDetails=results)

@app.route('/profilesCompany/<id>')
@login_required
def profilecompany(id):
    companyDetails = Companies.query.filter_by(id=id).first_or_404()
    #freelancersDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('ProfileCompany.html',companyDetails=companyDetails)


@app.route('/freelancers', methods=['GET', 'POST'])
@login_required
def freelancers():
    page = request.args.get('page', 1, type=int)
    freelancersDetails = Freelancers.query.order_by(Freelancers.name.desc()).paginate(page=page, per_page=5)
    return render_template("freelancers.html",freelancersDetails = freelancersDetails)

@app.route('/addFreelancers', methods=['GET', 'POST'])
@login_required
def addfreelancer():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        phone = request.form['phone']
        email = request.form['email']
        rating = request.form['rating']
        description = request.form['description']
 
        my_data = Freelancers(name, category, location, phone, email, rating, description)
        db.session.add(my_data)
        db.session.commit()
 
        return redirect('/freelancers')
    return render_template('addfreelancer.html')

@app.route('/editFreelancer/<id>', methods = ['GET', 'POST'])
@login_required
def editfreelancer(id):
    freelancerDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('updatefreelancer.html',freelancerDetails=freelancerDetails)

@app.route('/updateFreelancer/<id>', methods = ['GET', 'POST'])
@login_required
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
        my_data.rating = request.form['rating']
        my_data.description = request.form['description']
        db.session.commit()
        #flash("Employee Updated Successfully")
        return redirect('/freelancers')

@app.route('/deleteFreelancer/<id>', methods = ['GET', 'POST'])
@login_required
def deletefreelancer(id):
    my_data = Freelancers.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect("/freelancers")

@app.route('/profilesFreelancer/<id>')
@login_required
def profilefreelancer(id):
    freelancersDetails = Freelancers.query.filter_by(id=id).first_or_404()
    return render_template('ProfileFreelancer.html',freelancersDetails=freelancersDetails)


@app.route('/addCase')
@login_required
def addCase():
    companyDetails = Companies.query.all()
    return render_template('addCase.html', companyDetails = companyDetails)


if __name__ == "__main__":
    app.run(debug=True)