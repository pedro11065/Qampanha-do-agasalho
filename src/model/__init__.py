from src.model.services.auth.readEnv import *
from src.model.database import *
from src.model.classes import *

import psycopg2

class Db:

    def __init__(self):

        self.conn = self.connectDb()

        self.dbDonations = dbDonations(self)
        self.Donations = self.dbDonations

        self.dbUsers = dbUsers(self)
        self.Users = self.dbUsers

        self.dbTeams = dbTeams(self)
        self.Teams = self.dbTeams


    def connectDb(self):
        
        env = readEnv()
        try:
            conn = psycopg2.connect(
            host=env.get("PGHOST", "localhost"),
            database=env.get("PGDATABASE", "mydatabase"),
            user=env.get("PGUSER", "myuser"),
            password=env.get("PGPASSWORD", "mypass"),
            port=int(env.get("PGPORT", 5432))
            )
            return conn
        except Exception:
            raise
        