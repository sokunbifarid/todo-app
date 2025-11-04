from Flask import flask, render_template
import sqlite3
from helper import open_database, close_database, commit_database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update")
def update():
    return 0

@app.route("/delete")
def delete():
    return 0

@app.route("/write")
def write():
    return 0
