"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import requests
from .Auth import All_Auth


def request(url, params: dict[str, ...] = ""):
    auth = All_Auth
    response = requests.get(url, params=params, headers=auth, timeout=10)
    try:
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as err:
        return err, response.status_code
