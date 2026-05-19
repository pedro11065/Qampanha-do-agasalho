from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
#from src.model import Db
import json, os, base64, traceback
from datetime import datetime

class Donation:

    def __init__(self):
        pass

    def donate(self, donation_opt_id, user_id, team_id):

        from src.model import Db
        db = Db()
        success = db.donation.create(donation_opt_id, user_id, team_id)

        try:

            if success:
                print(cyan("[back-end]: ") + "Donation founded successfully!")
                return jsonify({'ok': True, 'message': 'Donation searched successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error searching for case: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the donation: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'Donation analysed successfully!'}), 201