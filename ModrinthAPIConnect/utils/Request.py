"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import requests
from ModrinthAPIConnect.Config import return_Auth

Auth = return_Auth()

def Request(url, params: str = ""):

    try:
        response = requests.get(url, params=params, headers=Auth, timeout=10)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as err:
        return err, response.status_code