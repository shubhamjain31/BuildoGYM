import os
from flask import Flask, request, redirect
from flask import render_template, flash, session
import json
import random
from datetime import datetime
from models import User, Packages, Shifts, Trainers, Payments, Attendance
from app import app, db

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

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
            entry = Packages(title=title,fee=fee,createdBy=userDetail,modifiedBy=userDetail,createdDate=date,modifiedDate=date,message=message)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('package.html',params=params)
          
@app.route("/shift_info", methods=["GET", "POST"])
def shift_info():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            title = request.form.get('title')
            sfrom = request.form.get('shiftFrom')
            sto = request.form.get('shiftTo')
            message = request.form.get('message')
            date = datetime.now()
            userDetail = User.query.filter_by(firstName=session['user'].capitalize()).first().email
            entry = Shifts(title=title,shiftFrom=sfrom,shiftTo=sto,createdBy=userDetail,modifiedBy=userDetail,createdDate=date,modifiedDate=date,message=message)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('shift.html',params=params)
    
@app.route("/trainer_info", methods=["GET", "POST"])
def trainer_info():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            email = request.form.get('email')
            phone = request.form.get('phone')
            address = request.form.get('address')
            city = request.form.get('city')
            gender = request.form.get('gender')
            zipcode = request.form.get('zipcode')
            cbox = request.form.get('cbox')
            for j in range(1):
                ls=random.randint(1111,9999)     
                trainerid=str(fname+lname+str(ls))
            date = datetime.now()
            entry = Trainers(firstName=fname,lastName=lname,email=email,mobileNo=phone,address=address,city=city,gender=gender,zip=zipcode,trainerId=trainerid,date=date)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('trainer.html',params=params)
    
@app.route("/payment_info", methods=["GET", "POST"])
def payment_info():
    uData = User.query.all()
    fname=[fn.firstName for fn in uData]
    lname=[ln.lastName for ln in uData]
    fullname=zip(fname,lname)
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
            name = request.form.get('username')
            month = request.form.get('month')
            date = request.form.get('date')
            amount = request.form.get('amount')
            message = request.form.get('message')
            entry = Payments(userName=name,month=month,date=date,amount=amount,message=message)
            db.session.add(entry)
            db.session.commit()
            flash('Data Saved Successfully')
    return render_template('payment.html',params=params,name=fullname)
    
@app.route("/attendance_info", methods=["GET", "POST"])
def attendance_info():
    uData = User.query.all()
    fname=[fn.firstName for fn in uData]
    lname=[ln.lastName for ln in uData]
    fullname=zip(fname,lname)
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
             name = request.form.get('username')
             date = request.form.get('date')
             message = request.form.get('message')
             entry = Attendance(userName=name,date=date,message=message)
             db.session.add(entry)
             db.session.commit()
             flash('Data Saved Successfully')
    return render_template('attendance.html',params=params,name=fullname)
    
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/test", methods=["GET", "POST"])
def test():
    if ('user' in session and session['user'] == params['admin_user']):
       v =  Attendance.query.all()
       print(v)
       return render_template('trainer.html', params=params)