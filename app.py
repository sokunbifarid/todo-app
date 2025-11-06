from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from helper import open_database, close_database, comit_database, check_if_contains_string

app = Flask(__name__)

username = "DEFAULT"
CATEGORIES = ["Normal", "Important", "Urgent"]

@app.route("/", methods=["GET"])
def index():
    print("indexed")
    data = get_todo_list()
    return render_template("index.html", categories=CATEGORIES, data=data)

@app.route("/get_todo_list", methods=["GET"])
def get_todo_list():
    global username
    data = [0,0,0]
    try:
        cursor = open_database()
        data = cursor.execute("SELECT * FROM todo_data WHERE username=?", [username]).fetchall()
        close_database()
    except ValueError as e:
        pass
    return data

@app.route("/modify/<id>", methods=["PUT"])
def modify(id):
    global username
    todo_name = request.form.get("todo_name")
    category = request.form.get("category")
    description = request.form.get("description")
    if not todo_name or not category or not description:
        return render_template("apology.html")
    if not check_if_contains_string(todo_name) or not check_if_contains_string(description):
        return render_template("apology.html")
    cursor = open_database()
    try:
        cursor.execute("UPDATE todo_data SET todo_name=?, category=?, description=? WHERE username=? AND id=?",[todo_name, category, description, username, id])
        comit_database()
        close_database()
        return redirect("/")
    except ValueError as e:
        render_template("apology.html")

@app.route("/delete/<id>", methods=["GET", "DELETE"])
def delete(id):
    print("delete function called")
    global username
    cursor = open_database()
    try:
        cursor.execute("DELETE FROM todo_data WHERE id=? AND username=?", [id, username])
        comit_database()
        close_database()
        print("pass")
        return redirect(url_for("index"))
        print("passat")
    except ValueError as e:
        render_template("apology.html")

@app.route("/write", methods=["POST"])
def write():
    global username
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
