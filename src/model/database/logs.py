from src.config.colors import *
from uuid import uuid4
from datetime import datetime

class dbLogs:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    def search(self):

        cur = self.conn.cursor()

        cur.execute(f"SELECT * FROM donation_logs")
        self.conn.commit() ; rows = cur.fetchall()
        cur.close()

        logs = []

        for row in rows:
            logs.append(row)

        return logs


    def create(self, donation_opt_id, user_id, quant, browser_language, screen_resolution, timezone, referrer, ip_addr, user_agent, http_status, is_success, error_message):

        try:
            cur = self.conn.cursor()

            print(blue("[Database]: ") + "registering donation log...")
            log_id = str(uuid4())
            created_at = datetime.now()

            cur.execute(
                """INSERT INTO donation_logs (log_id, user_id, donation_opt_id, quantity, ip_address, user_agent, browser_language, screen_resolution, timezone, session_referrer, http_status, is_success, error_message, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    log_id,
                    user_id,
                    donation_opt_id,
                    quant,
                    ip_addr,
                    user_agent,
                    browser_language,
                    screen_resolution,
                    timezone,
                    referrer,
                    http_status,
                    is_success,
                    error_message,
                    created_at
                ),
            )

            self.conn.commit()
            cur.close()

            print(green("[Database]: ") + "Donation log registered successfully!")
            return True
        
        except Exception as e:
            print(red("[ERROR]: ") + f"Could not register donation log: {e}")
            self.conn.rollback()
            return False
