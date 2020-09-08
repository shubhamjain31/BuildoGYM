import os
from flask import Flask, request, redirect
from flask import render_template, session
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
    
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "gymdb.db"))


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

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
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template('payment.html',params=params)
    
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8087, debug=True)
