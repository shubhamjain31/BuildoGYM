import os
from flask import Flask, request, redirect
from flask import render_template, flash, session
import json
import random
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import model.User

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
    
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "gymdb.db"))


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html',params=params)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('dashboard.html', params=params)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            return render_template('dashboard.html', params=params)
    return render_template('signin.html',params=params)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            package = request.form.get('package')
            shift = request.form.get('shift')
            email = request.form.get('email')
            password = request.form.get('password')
            phone = request.form.get('phone')
            address = request.form.get('address')
            city = request.form.get('city')
            gender = request.form.get('gender')
            zipcode = request.form.get('zipcode')
            cbox = request.form.get('cbox')
            for j in range(1):
                ls=random.randint(1111,9999)     
                userid=str(fname+lname+str(ls))
            date = datetime.now()
            entry = User(firstName=fname,lastName=lname,package=package,shift=shift,email=email,password=password,mobileNo=phone,address=address,city=city,gender=gender,zip=zipcode,userId=userid,date=date)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('signup.html',params=params)

@app.route("/package_info", methods=["GET", "POST"])
def package_info():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            title = request.form.get('title')
            fee = request.form.get('fee')
            message = request.form.get('message')
            date = datetime.now()
            userDetail = User.query.filter_by(firstName=session['user'].capitalize()).first().email
            print(userDetail)
            entry = Packages(title=title,fee=fee,createdBy=userDetail,modifiedBy=userDetail,createdDate=date,modifiedDate=date,message=message)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('package.html',params=params)
          
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/test", methods=["GET", "POST"])
def test():
    if ('user' in session and session['user'] == params['admin_user']):
        u = Packages.query.all()
        print(u)
        return render_template('dashboard.html', params=params)

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=8087, debug=True)
