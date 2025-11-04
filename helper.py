import sqlite3
import string

database_path = "todo_database.db"

connection = []
cursor = []

def open_database():
    global connection
    global cursor
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    return cursor

def close_database():
    global connection
    if connection:
        connection.close()
    else:
        print("database connection not established")

def comit_database():
    global connection
    if connection:
        connection.commit()
    else:
        print("database connection not established")

def check_if_contains_string(value):
    all_text = string.ascii_letters
    for i in value:
        if i in all_text:
            return True
    return False

