"""
This module provides a function for making HTTP GET requests using the `requests` library.
"""

import requests

All_Auth = {}

def set_Auth(Token: str = None, GithubUsername: str = None, ProjectName: str = None, Email: str = None):
    """
    The function sets the authentication and user agent headers for API requests. It takes in a token, Github
    username, project name, and email as parameters and combines them into a dictionary of headers.
    
    ---
    
    ### ---Parameters---
    
    :param Token: The authentication token to be used in API requests (HIGHLY RECOMMENDED TO USE A CSV FILE TO STORE TOKENS)
    :type Token: str (optional)
    
    :param GithubUsername: The Github username to be used in the user agent header of API requests
    :type GithubUsername: str (optional)
    
    :param ProjectName: The project name to be used in the user agent header of API requests
    :type ProjectName: str (optional)
    
    :param Email: The email to be used in the user agent header of API requests
    :type Email: str (optional)
    
    :return: None
    """
    
    global All_Auth
    # set authentication
    User_Auth = {'Authorization': Token}
    # set user agent
    User_Agent = {'User-Agent': f"{GithubUsername}/{ProjectName} ({Email})"}
    # combine headers
    All_Auth = User_Auth | User_Agent

def Request(url, params: str = ""):
    Auth = All_Auth
    try:
        response = requests.get(url, params=params, headers=Auth, timeout=10)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as err:
        return err, response.status_code