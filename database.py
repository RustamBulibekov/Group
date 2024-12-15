import sqlite3
import os

def connecting_with_database(filename: str):
    try:
        connecting = sqlite3.connect(filename)
    except sqlite3.Error as error:
        return f'{error} error'
    else:
        return connecting


def execute(statement, column_values=None):
    with connecting_with_database("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(statement, column_values or ())
        connection.commit()


def create_table():
    statement = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT NOT NULL',
        'email': 'TEXT NOT NULL UNIQUE',
        'password': 'TEXT NOT NULL'
    }
    columns = [f'{column_name} {data_type}' for column_name, data_type in statement.items()]
    execute(f"""CREATE TABLE IF NOT EXISTS users ({','.join(columns)});""")


def add_user(username: str, email: str, password: str):
    data = {
        'username': username,
        'email': email,
        'password': password
    }
    placeholders = ','.join('?' * len(data))
    columns_names = ','.join(data.keys())
    columns_value = tuple(data.values())
    execute(f"""INSERT OR IGNORE INTO users ({columns_names}) VALUES ({placeholders})""", columns_value)


def select_id(user_id: int):
    with connecting_with_database("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM users WHERE id={user_id}""")
        result = cursor.fetchone()
        return result


def select_username(username: str):
    with connecting_with_database("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM users WHERE username = ?""", (username,))
        result = cursor.fetchone()
        return result


def select_email(email: str):
    with connecting_with_database("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM users WHERE email = ?""", (email,))
        result = cursor.fetchone()
        return result


create_table()
add_user('imanali', 'imanalitussip@gmail.com', 'qwerty123')
user = select_id(1)
print(user)
