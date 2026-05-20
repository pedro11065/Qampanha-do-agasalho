from src.config.colors import *
from uuid import uuid4
from datetime import datetime

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

    
    def create(self, donation_opt_id, user_id, quant):

        try:
            cur = self.conn.cursor()
            
            print(blue("[Database]: ") + "registering donation...")
            donation_id = str(uuid4()) ; donation_time = datetime.now()

            cur.execute(
                """INSERT INTO donations (donation_id, donation_opt_id, user_id, donation_time, quant)
                    VALUES (%s, %s, %s, %s, %s)""",
                (donation_id, donation_opt_id, user_id,donation_time , quant),
            )
            
            self.conn.commit()
            cur.close()

            print(green("[Database]: ") + "Donation registered successfully!")
            return True
        except Exception as e:
            print(red("[ERROR]: ") + f"Could not register donation: {e}")
            self.conn.rollback()
            return False
