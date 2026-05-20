from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
#from src.model import Db
import json, os, base64, traceback
from datetime import datetime

class Donation:

    def __init__(self):
        pass

    def search(self):

        from src.model import Db
        db = Db()
        success = db.Donations.search()

        try:

            if success:
                print(cyan("[back-end]: ") + "Donation founded successfully!")
                return jsonify({'data':success, 'ok': True, 'message': 'Donation searched successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error searching for donation: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the donation: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'Donation analysed successfully!'}), 201
    


    def create(self, data):

        from src.model import Db
        db = Db()

        donation_opt_id = data["donation_opt_id"]
        user_id = data["user_id"]
        quant = data["quant"]

        success = db.Donations.create(donation_opt_id, user_id, quant)

        try:

            if success:
                print(cyan("[back-end]: ") + "Donation created successfully!")
                return jsonify({'ok': True, 'message': 'Donation created successfully!'}), 201

            else:
                raise Exception("Database insertion failed")

        except Exception as e:
        
            print(red("[ERROR]: ") + f"Error registering donation: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the donation: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'Donation analysed successfully!'}), 201