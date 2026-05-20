from src.config.colors import *
from uuid import uuid4

class dbUsers:

    def __init__(self, db):
        # keep a reference to the parent Db and its connection
        self.db = db
        self.conn = db.conn

    def searchByTeam(self, team_id):

        cur = self.conn.cursor()

        cur.execute(f"""SELECT user_team.user_id, users.user_name
                    FROM user_team 
                    LEFT JOIN users ON user_team.user_id = users.user_id
                    WHERE user_team.team_id = '{team_id}'""")
        
        self.conn.commit() ; rows = cur.fetchall()
        cur.close()

        users = []

        for row in rows:
            users.append(row)

        return users
    
    

    def create(self, user_name, team_id):

        try:
            cur = self.conn.cursor()

            print(blue("[Database]: ") + "registering user...")
            user_id = str(uuid4())

            cur.execute(
                """INSERT INTO users (user_id, user_name) VALUES (%s, %s)""",
                (user_id, f"{user_name}"),
            )
            print(blue("[Database]: ") + "user created!")
            
            #----------------------------------------------------------------
            #----------------------------------------------------------------

            print(blue("[Database]: ") + "registering user in a team...")
            user_team_id = str(uuid4())

            cur.execute(
                """INSERT INTO user_team (user_team_id, team_id, user_id) VALUES (%s, %s, %s)""",
                (user_team_id, team_id, user_id),
            )
            print(blue("[Database]: ") + "team - User created!")

            self.conn.commit()
            cur.close()

            #----------------------------------------------------------------
            #----------------------------------------------------------------

            print(green("[Database]: ") + "User registered successfully!")
            return True
        except Exception as e:
            print(red("[ERROR]: ") + f"Could not register user: {e}")
            self.conn.rollback()
            return False

