from flask import jsonify
from src.model.services.Qapp import *
from src.config.colors import *
import json, traceback
from datetime import datetime

class Log:

    def __init__(self):
        pass

    def search(self):

        from src.model import Db
        db = Db()
        success = db.Logs.search()

        try:

            if success:
                print(cyan("[back-end]: ") + "Logs found successfully!")
                return jsonify({'data':success, 'ok': True, 'message': 'Logs searched successfully!'}), 201

            else:
                print(red("[ERROR]: ") + "No logs found or empty result")
                return jsonify({'data':[], 'ok': True, 'message': 'No logs found'}), 200

        except Exception as e:
            print(red("[ERROR]: ") + f"Error searching logs: {str(e)}")
            traceback.print_exc()
            return jsonify({'ok': False, 'error': f'Error while trying to search logs: {str(e)}'}), 500

        return jsonify({'ok': True, 'message': 'Logs analysed successfully!'}), 201


    def create(self, data):

        from src.model import Db
        db = Db()

        user_id = data.get('user_id')
        donation_opt_id = data.get('donation_opt_id')
        quantity = data.get('quantity')
        ip_address = data.get('ip_address')
        user_agent = data.get('user_agent')

        browser_info = data.get('browser_info', {}) or {}
        browser_language = browser_info.get('browser_language', '')
        screen_resolution = browser_info.get('screen_resolution', '')
        timezone = browser_info.get('timezone', '')
        session_referrer = browser_info.get('referrer', '')

        http_status = data.get('http_status')
        is_success = data.get('is_success', True)
        error_message = data.get('error_message')

        try:

            success = db.Logs.create(
                user_id=user_id,
                donation_opt_id=donation_opt_id,
                quant=quantity,
                ip_addr=ip_address,
                user_agent=user_agent,
                browser_language=browser_language,
                screen_resolution=screen_resolution,
                timezone=timezone,
                referrer=session_referrer,
                http_status=http_status,
                is_success=is_success,
                error_message=error_message,
            )

            if success:
                print(cyan("[back-end]: ") + "Log created successfully!")
                return True
            else:
                print(red("[ERROR]: ") + "Log creation returned False")
                return False

        except Exception as e:
            print(red("[ERROR]: ") + f"Error creating log: {str(e)}")
            traceback.print_exc()
            return False
