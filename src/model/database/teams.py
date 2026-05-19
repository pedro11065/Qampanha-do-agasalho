from src.config.colors import *

class dbTeams:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    def search(self):

        cur = self.conn.cursor()

        cur.execute(f"SELECT * FROM teams")
        self.conn.commit() ; rows = cur.fetchall()
        cur.close()

        teams = []

        for row in rows:
            teams.append(row)

        return teams

