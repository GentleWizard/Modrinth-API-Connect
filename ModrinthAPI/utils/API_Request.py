"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import json
import os

import requests

current_dir = os.path.dirname(__file__)

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, "auth.json")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        auth = json.load(file)
except FileNotFoundError:
    auth = None


def request(
    url: str,
    method: str,
    params: dict[str, ...] | None = None,
    data: dict[str, ...] | None = None,
    files: dict[str, ...] | None = None,
):
    """
    Sends an HTTP request to the specified URL using the specified method.

    Args:
        url (str): The URL to send the request to.
        method (str): The HTTP method to use for the request (e.g. GET, POST, PATCH, DELETE).
        params (dict[str, ...], optional): The query parameters to include in the request. Defaults to {}.
        data (dict[str, ...] | None, optional): The data to include in the request body. Defaults to None.
        files (dict[str, ...] | None, optional): The files to include in the request body. Defaults to None.

    Returns:
        tuple: A tuple containing the response data (if successful) or error message (if unsuccessful) and the HTTP status code.
    """
    if params is None:
        params = {}
    if method == "GET":
        response = requests.get(url, params=params, headers=auth, timeout=10)
        try:
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.RequestException as err:
            return err, response.status_code

    elif method == "Patch":
        response = requests.patch(url, json=data, headers=auth, timeout=10, files=files)
        try:
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as err:
            return err, response.status_code

    # TODO: Add POST and DELETE methods
    elif method == "POST":
        pass

    elif method == "Delete":
        pass
