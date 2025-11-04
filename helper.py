import sqlite3

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


