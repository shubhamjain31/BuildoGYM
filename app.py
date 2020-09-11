from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json
from flask_mail import Mail

app = Flask(__name__)

with open('config.json', 'r') as c:
	params = json.load(c)["params"]

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "gymdb.db"))

app.secret_key = 'super-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#used for continue and break statement dependencies
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)

db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()
    from views import *
    app.run(host='0.0.0.0', port=8087, debug=True)