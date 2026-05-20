from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
#from src.model import Db
import json, os, base64, traceback
from datetime import datetime

class Team:

    def __init__(self):
        pass

    def search(self):

        from src.model import Db
        db = Db()
        success = db.Teams.search()

        try:

            if success:
                print(cyan("[back-end]: ") + "Team founded successfully!")
                return jsonify({'data':success, 'ok': True, 'message': 'Team searched successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error searching for team: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the team: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'team analysed successfully!'}), 201
    