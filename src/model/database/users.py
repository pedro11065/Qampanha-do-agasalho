from src.config.colors import *

class dbUsers:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    def search(self):

        cur = self.conn.cursor()

        cur.execute(f"SELECT * FROM users")
        self.conn.commit() ; rows = cur.fetchall()
        cur.close()

        users = []

        for row in rows:
            users.append(row)

        return users

