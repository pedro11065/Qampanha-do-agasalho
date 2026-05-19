from src.config.colors import *

class dbDonations:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    def search(self):

        cur = self.conn.cursor()

        cur.execute(f"SELECT * FROM donation_opt")
        self.conn.commit() ; rows = cur.fetchall()
        cur.close()

        donation_opt = []

        for row in rows:
            donation_opt.append(row)

        return donation_opt

    
    def create(self, donation_opt_id, user_id, team_id):

        try:
            cur = self.conn.cursor()

            print(blue("[Database]: ") + "registering case...")

            cur.execute(
                """INSERT INTO donations (donation_opt_id, user_id, team_id)
                    VALUES (%s, %s, %s)""",
                (donation_opt_id, user_id, team_id),
            )
            
            self.conn.commit()
            cur.close()

            print(green("[Database]: ") + "Donation registered successfully!")
            return True
        except Exception as e:
            print(red("[ERROR]: ") + f"Could not register donation: {e}")
            self.conn.rollback()
            return False
