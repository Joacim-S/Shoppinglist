from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    db.session.execute("INSERT INTO users (name) VALUES ('tester')")
    result = db.session.execute('SELECT name FROM users')
    userlist = result.fetchall()
    return render_template("index.html", users=users)