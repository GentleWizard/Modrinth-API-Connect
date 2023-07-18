"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import requests
import json
import os

current_dir = os.path.dirname(__file__)

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'auth.json')

try:
    with open(file_path, 'r') as file:
        auth = json.load(file)
except FileNotFoundError:
    auth = None


def request(url: str, method: str, params: dict[str, ...] = "", data: dict[str, ...] = None,
            files: dict[str, ...] = None):
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

