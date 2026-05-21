import requests
import json
from typing import Dict, Any, Optional
from src.config.colors import *

def reloadApp() -> Dict[str, Any]:

    # Qlik automation endpoint URL
    url = 'https://qampanhadoagasalho.se.qlikcloud.com/api/v1/automations/ee9760b6-44c7-48b8-adc1-f06f0db29a47/actions/execute'
    
    # Execution token for authentication
    token = 'lRko6BToBETcpYZYtQTtKFYBmVOvBgNKQNDPEYtf63vjVsxPAO8vlPffTYRwOWdQ'
    
    # Headers for the request
    headers = {
        'X-Execution-Token': token,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:

        print(cyan("[back-end]: ") + "Doing request to update qlik app...")
        response = requests.post(url, headers=headers, timeout=30)
        
        response.raise_for_status()
        
        try:
            result = response.json()
        except json.JSONDecodeError:
       
            result = {
                'status': 'success',
                'message': 'Automation triggered successfully',
                'response_text': response.text,
                'status_code': response.status_code
            }
        
        print(green("[Qlik]: ") + "App reload automation triggered successfully!")
        
        return result

    except Exception as e:

        print(red("[ERROR]: ") + f"Unexpected error occurred: {e}")
        error_msg = f"Unexpected error occurred: {e}"
        return {
            'status': 'error',
            'error': error_msg,
            'error_type': 'unexpected_error'
        }


def reloadAppAsync() -> None:
    """
    Triggers the Qlik automation asynchronously without waiting for response details.
    """
    url = 'https://qampanhadoagasalho.se.qlikcloud.com/api/v1/automations/ee9760b6-44c7-48b8-adc1-f06f0db29a47/actions/execute'
    token = 'lRko6BToBETcpYZYtQTtKFYBmVOvBgNKQNDPEYtf63vjVsxPAO8vlPffTYRwOWdQ'
    
    headers = {
        'X-Execution-Token': token,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, timeout=5)
        if response.status_code in [200, 201, 202]:
            print(green("[Qlik]: ") + "App reload automation triggered!")
        else:
            print(cyan("[back-end]: ") + f"Automation triggered with status code: {response.status_code}")
    except Exception as e:
        print(red("[ERROR]: ") + f"Failed to trigger automation: {e}")

