"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import requests
from .Auth import All_Auth


def request(url: str, method: str, params: dict[str, ...] = "", data: dict[str, ...] = None, files: dict[str, ...] = None):
    auth = All_Auth
    if method == 'GET':
        response = requests.get(url, params=params, headers=auth, timeout=10)
        try:
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as err:
            return err, response.status_code

    elif method == 'Patch':
        response = requests.patch(url, json=data, headers=auth, timeout=10, files=files)
        try:
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as err:
            return err, response.status_code

    elif method == 'POST':
        pass

    elif method == 'Delete':
        pass
