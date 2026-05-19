from src.config.colors import *

class dbDonation:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    # def search(self, user_name):

    #     cur = self.conn.cursor()

    #     cur.execute(f"SELECT users FROM cases WHERE user_name = '{user_name}'")
    #     self.conn.commit() ; rows = cur.fetchall()
    #     cur.close()

    #     cases = []

    #     for row in rows:
    #         cases.append(row)

    #     return cases
    
    def create(self, donation_opt_id, user_id, team_id):

        try:
            cur = self.conn.cursor()

            print(blue("[Database]: ") + "registering case...")

            cur.execute(
                """INSERT INTO cases (donation_opt_id, user_id, team_id)
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
