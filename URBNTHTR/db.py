import os
import re
import sqlite3

SQLITE_PATH = os.path.join(os.path.dirname(__file__), 'urbn.db')

class Database:

    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_PATH)

    def select(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchall()

    def execute(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        self.conn.commit()
    def create_user(self, name, email, encrypted_password):
        self.execute('INSERT INTO users (name, email, encrypted_password) VALUES (?, ?, ?)',
                     [name, email, encrypted_password])

    def get_user(self, email):
        data = self.select('SELECT * FROM users WHERE email=?', [email])
        if data:
            d = data[0]
            return {
                'name': d[0],
                'email': d[1],
                'encrypted_password': d[2],
                'user_id': d[3]
            }
        else:
            return None

    def close(self):
        self.conn.close()