import os
from flask import Flask, request, redirect
from flask import render_template
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return params['gym_name']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8087, debug=True)
