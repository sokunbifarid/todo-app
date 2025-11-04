from flask import Flask, render_template, request, redirect
import sqlite3
from helper import open_database, close_database, comit_database, check_if_contains_string

app = Flask(__name__)

CATEGORIES = ["Normal", "Important", "Urgent"]

@app.route("/", methods=["GET"])
def index():
    username = "DEFAULT"
    data = []
    try:
        cursor = open_database()
        data = cursor.execute("SELECT * FROM todo_data WHERE username=?", [username]).fetchall()
        print("data: " + str(data))
        close_database()
    except ValueError as e:
        pass
    return render_template("index.html", categories=CATEGORIES, data=data)

@app.route("/modify", methods=["PUT"])
def modify():
    return 0

@app.route("/delete", methods=["DELETE"])
def delete():
    return 0

@app.route("/write", methods=["POST"])
def write():
    username = "DEFAULT"
    todo_name = request.form.get("todo_name")
    category = request.form.get("category")
    description = request.form.get("description")
    if not todo_name or not category or not description:
        return render_template("apology.html")
    if not check_if_contains_string(todo_name) or not check_if_contains_string(description):
        return render_template("apology.html")
    cursor = open_database()
    try:
        cursor.execute("INSERT INTO todo_data (username, todo_name, category, description) VALUES(?,?,?,?)", (username, todo_name, category, description))
        comit_database()
        close_database()
        return redirect("/")
    except ValueError as e:
        render_template("apology.html")
    return 0
