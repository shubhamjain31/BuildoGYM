from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "gymdb.db"))

app.secret_key = 'super-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    db.create_all()
    from main import *
    app.run(host='0.0.0.0', port=8087, debug=True)