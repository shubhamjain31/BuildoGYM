import os
from flask import Flask, request, redirect
from flask import render_template, flash, session
import json
import random
from datetime import datetime
from models import User, Packages, Shifts, Trainers, Payments, Attendance, Contacts
from app import app, db, mail

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
    return render_template('register.html',params=params)

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
    
@app.route("/package_show", methods=["GET", "POST"])
def package_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = Packages.query.all()
       return render_template('packageList.html', params=params,alldata=alldata)
       
@app.route("/package_delete/<string:sno>", methods = ['GET', 'POST'])
def package_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = Packages.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/package_show')
    
@app.route("/package_edit/<string:sno>", methods=["GET", "POST"])
def package_edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
            title = request.form.get('title')
            fee = request.form.get('fee')
            message = request.form.get('message')
            date = datetime.now()
            userDetail = User.query.filter_by(firstName=session['user'].capitalize()).first().email
            uData = Packages.query.filter_by(sno=sno).first()
            uData.title = title
            uData.fee = fee
            uData.modifiedBy = userDetail
            uData.modifiedDate = date
            uData.message = message
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/package_edit/'+sno)
       data = Packages.query.filter_by(sno=sno).first()
       return render_template('package_edit.html', params=params,data=data,sno=sno)
       
@app.route("/shift_show", methods=["GET", "POST"])
def shift_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = Shifts.query.all()
       return render_template('shiftList.html', params=params,alldata=alldata)
       
@app.route("/shift_delete/<string:sno>", methods = ['GET', 'POST'])
def shift_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = Shifts.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/shift_show')
    
@app.route("/shift_edit/<string:sno>", methods=["GET", "POST"])
def shift_edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
            title = request.form.get('title')
            sfrom = request.form.get('shiftFrom')
            sto = request.form.get('shiftTo')
            message = request.form.get('message')
            date = datetime.now()
            userDetail = User.query.filter_by(firstName=session['user'].capitalize()).first().email
            uData = Shifts.query.filter_by(sno=sno).first()
            uData.title = title
            uData.shiftFrom = sfrom
            uData.shiftTo = sto
            uData.modifiedBy = userDetail
            uData.modifiedDate = date
            uData.message = message
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/shift_edit/'+sno)
       data = Shifts.query.filter_by(sno=sno).first()
       return render_template('shift_edit.html', params=params,data=data,sno=sno)
       
@app.route("/user_show", methods=["GET", "POST"])
def user_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = User.query.all()
       return render_template('userList.html', params=params,alldata=alldata)
       
@app.route("/user_delete/<string:sno>", methods = ['GET', 'POST'])
def user_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = User.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/user_show')
    
@app.route("/user_edit/<string:sno>", methods=["GET", "POST"])
def user_edit(sno):
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
            date = datetime.now()
            uData = User.query.filter_by(sno=sno).first()
            uData.firstName = fname
            uData.lastName = lname
            uData.package = package
            uData.shift = shift
            uData.email = email
            uData.mobileNo = phone
            uData.address = address
            uData.city = city
            uData.gender = gender
            uData.zip = zipcode
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/user_edit/'+sno)
       data = User.query.filter_by(sno=sno).first()
       return render_template('user_edit.html', params=params,data=data,sno=sno)
       
@app.route("/trainer_show", methods=["GET", "POST"])
def trainer_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = Trainers.query.all()
       return render_template('trainerList.html', params=params,alldata=alldata)
       
@app.route("/trainer_delete/<string:sno>", methods = ['GET', 'POST'])
def trainer_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = Trainers.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/trainer_show')
    
@app.route("/trainer_edit/<string:sno>", methods=["GET", "POST"])
def trainer_edit(sno):
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
            date = datetime.now()
            uData = Trainers.query.filter_by(sno=sno).first()
            uData.firstName = fname
            uData.lastName = lname
            uData.email = email
            uData.mobileNo = phone
            uData.address = address
            uData.city = city
            uData.gender = gender
            uData.zip = zipcode
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/trainer_edit/'+sno)
       data = Trainers.query.filter_by(sno=sno).first()
       return render_template('trainer_edit.html', params=params,data=data,sno=sno)
       
@app.route("/attendance_show", methods=["GET", "POST"])
def attendance_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = Attendance.query.all()
       return render_template('attendanceList.html', params=params,alldata=alldata)
       
@app.route("/attendance_delete/<string:sno>", methods = ['GET', 'POST'])
def attendance_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = Attendance.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/attendance_show')
    
@app.route("/attendance_edit/<string:sno>", methods=["GET", "POST"])
def attendance_edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
            name = request.form.get('name')
            date = request.form.get('date')
            message = request.form.get('message')
            cbox = request.form.get('cbox')
            uData = Attendance.query.filter_by(sno=sno).first()
            uData.userName = name
            uData.date = date
            uData.message = message
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/attendance_edit/'+sno)
       data = Attendance.query.filter_by(sno=sno).first()
       return render_template('attendance_edit.html', params=params,data=data,sno=sno)
       
@app.route("/payment_show", methods=["GET", "POST"])
def payment_show():
    if ('user' in session and session['user'] == params['admin_user']):
       alldata = Payments.query.all()
       return render_template('paymentList.html', params=params,alldata=alldata)
       
@app.route("/payment_delete/<string:sno>", methods = ['GET', 'POST'])
def payment_delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        data = Payments.query.filter_by(sno=sno).first()
        db.session.delete(data)
        db.session.commit()
        flash('Data Deleted Successfully')
    return redirect('/payment_show')
    
@app.route("/payment_edit/<string:sno>", methods=["GET", "POST"])
def payment_edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
       if request.method == 'POST':
            name = request.form.get('username')
            month = request.form.get('month')
            date = request.form.get('date')
            amount = request.form.get('amount')
            message = request.form.get('message')
            userDetail = User.query.filter_by(firstName=session['user'].capitalize()).first().email
            uData = Payments.query.filter_by(sno=sno).first()
            uData.userName = name
            uData.month = month
            uData.date = date
            uData.amount = amount
            uData.message = message
            db.session.commit()
            flash('Data Updated Successfully')
            return redirect('/payment_edit/'+sno)
       data = Payments.query.filter_by(sno=sno).first()
       uData = User.query.all()
       fname=[fn.firstName for fn in uData]
       lname=[ln.lastName for ln in uData]
       fullname=zip(fname,lname)
       return render_template('payment_edit.html', params=params,data=data,sno=sno,fullname=fullname)
       
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/about_us", methods=["GET", "POST"])
def about_us():
	return render_template('aboutUs.html', params=params)
	
@app.route("/contact_us", methods = ['GET', 'POST'])
def contact_us():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        flash('Data Saved Successfully')
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + phone
                          )
    return render_template('contactUs.html', params=params)

@app.route("/test", methods=["GET", "POST"])
def test():
	print(session.get('user'))
	return "OK"