from flask import Flask, render_template
import sqlite3
from helper import open_database, close_database, comit_database

app = Flask(__name__)

CATEGORIES = ["Normal", "Important", "Urgent"]

@app.route("/")
def index():
    return render_template("index.html", categories=CATEGORIES)

@app.route("/update")
def update():
    return 0

@app.route("/delete")
def delete():
    return 0

@app.route("/write")
def write():
    username = "DEFAULT"
    todo_name = request.form.get("todo_name")
    category = request.form.get("category")
    description = request.form.get("description")
    if not todo_name or not category or not description:
        render_template("apology.html")
    cursor = open_database()
    try:
        cursor.execute("INSERT INTO todo_data (username, todo_name, category, description) VALUES(?,?,?,?)", (username, todo_name, category, description))
        comit_database()
        close_database()
    except ValueError as e:
        render_template("apology.html")
    return 0
