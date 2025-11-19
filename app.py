from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from helper import open_database, close_database, comit_database, check_if_contains_string
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "super secret key"

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

username = "DEFAULT"
CATEGORIES = ["Normal", "Important", "Urgent"]

@app.route("/", methods=["GET"])
@login_required
def index():
    data = get_todo_list()
    return render_template("index.html", categories=CATEGORIES, data=data)

@app.route("/get_todo_list", methods=["GET"])
@login_required
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

@app.route("/modify/<id>/<todo_name>/<category>/<description>", methods=["PUT"])
@login_required
def modify(id, todo_name, category, description):
    global username
    if not todo_name or not category or not description:
        return render_template("apology.html")
    if not check_if_contains_string(todo_name) or not check_if_contains_string(description):
        return render_template("apology.html")
    cursor = open_database()
    try:
        cursor.execute("UPDATE todo_data SET todo_name=?, category=?, description=? WHERE username=? AND id=?",[todo_name, category, description, username, id])
        comit_database()
        close_database()
        return ("sucess", 200)
    except ValueError as e:
        return render_template("apology.html")

@app.route("/delete/<id>", methods=["GET", "DELETE"])
@login_required
def delete(id):
    print("delete function called")
    global username
    cursor = open_database()
    try:
        cursor.execute("DELETE FROM todo_data WHERE id=? AND username=?", [id, username])
        comit_database()
        close_database()
        return ("sucess", 200)
    except ValueError as e:
        return render_template("apology.html")

@app.route("/write", methods=["POST"])
@login_required
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
        return redirect(url_for("index"))
    except ValueError as e:
        return render_template("apology.html")

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def user_loader(id):
    cursor = open_database()
    userdata = cursor.execute("SELECT * FROM users WHERE id=?", id).fetchone()
    close_database()
    if userdata:
        print("userdata: " + str(userdata))
        return User(userdata[0], userdata[1], userdata[2])
    return None

@login_manager.request_loader
def request_loader(request):
   # cursor = open_database()
   # userdata = cursor.execute("SELECT * FROM users WHERE id=?", id).fetchone()
   # close_database()
   # if userdata:
   #     print("userdata: " + str(userdata))
   #     return User(userdata[0], userdata[1], userdata[2])
   # return None
    pass

@app.route("/login", methods=["GET", "POST"])
@login_required
def login():
    if method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        cursor = open_database()
        userdata = cursor.execute("SELECT * FROM users WHERE email=?", email).fetchone()
        close_database()
        print("userdata login: " + str(userdata))
        if userdata and check_password_hash(userdata[2], password):
            user = User(userdata[0], userdata[1], userdata[2])
            login_user(user)
            return redirect("/")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


