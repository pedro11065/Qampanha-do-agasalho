from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
#from src.model import Db
import json, os, base64, traceback
from datetime import datetime

class User:

    def __init__(self):
        pass

    def search(self):

        from src.model import Db
        db = Db()
        success = db.Users.search()

        try:

            if success:
                print(cyan("[back-end]: ") + "User founded successfully!")
                return jsonify({'data':success, 'ok': True, 'message': 'user searched successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error searching for user: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the user: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'User analysed successfully!'}), 201
    


    def create(self, data):

        from src.model import Db
        db = Db()

        user_name = data["user_name"]
        team_id = data["team_id"]

        success = db.Users.create(user_name, team_id)

        try:

            if success:
                print(cyan("[back-end]: ") + "User created successfully!")
                return jsonify({'ok': True, 'message': 'User created successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error creating user: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to create user: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'Donation analysed successfully!'}), 201