from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
from src.model.classes.log import *
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

        donation_opt_id = data[0]["donation_opt_id"]
        user_id = data[0]["user_id"]
        quant = data[0]["quant"]

        browser_info = data[0].get('browser_info', {})
        ip_addr = data[1]
        user_agent = data[2]

        # First, create the donation (this is the main transaction)
        try:
            donation_created = db.Donations.create(donation_opt_id, user_id, quant)

            if not donation_created:
                raise Exception("Database insertion failed for donation")

            # After donation is successfully created, create a non-blocking log
            try:
                log_payload = {
                    'user_id': user_id,
                    'donation_opt_id': donation_opt_id,
                    'quantity': quant,
                    'ip_address': ip_addr,
                    'user_agent': user_agent,
                    'browser_info': browser_info,
                    'http_status': 200,
                    'is_success': True,
                }

                # Use db.Logs to avoid Flask response wrapping and to keep simple return
                db.Logs.create(
                    donation_opt_id=log_payload.get('donation_opt_id'),
                    user_id=log_payload.get('user_id'),
                    quant=log_payload.get('quantity'),
                    browser_language=browser_info.get('browser_language', ''),
                    screen_resolution=browser_info.get('screen_resolution', ''),
                    timezone=browser_info.get('timezone', ''),
                    referrer=browser_info.get('referrer', ''),
                    ip_addr=log_payload.get('ip_address'),
                    user_agent=log_payload.get('user_agent'),
                    http_status=log_payload.get('http_status'),
                    is_success=log_payload.get('is_success'),
                    error_message=None,
                )
            except Exception as le:
                print(red("[ERROR]: ") + f"Error creating donation log: {le}")

            return jsonify({'ok': True, 'message': 'Donation created successfully!'}), 201

        except Exception as e:
            print(red("[ERROR]: ") + f"Error registering donation: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to register the donation: {str(e)}'}), 500
