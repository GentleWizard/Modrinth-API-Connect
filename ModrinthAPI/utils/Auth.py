import json
import os


def set_auth(Token: str = None, GithubUsername: str = None, ProjectName: str = None, Email: str = None):
    """
    The function sets the authentication and user agent headers for API requests. It takes in a token, GitHub
    username, project name, and email as parameters and combines them into a dictionary of headers.

    ---

    ### ---Parameters---

    :param Token: The authentication token to be used in API requests (HIGHLY RECOMMENDED TO USE A CSV FILE TO STORE
    TOKENS)
    :type Token: str (optional)

    :param GithubUsername: The GitHub username to be used in the user agent header of API requests
    :type GithubUsername: str (optional)

    :param ProjectName: The project name to be used in the user agent header of API requests
    :type ProjectName: str (optional)

    :param Email: The email to be used in the user agent header of API requests
    :type Email: str (optional)

    :return: None
    """
    try:
        with open('ModrinthAPI/auth.json', 'r') as file:
            auth = json.load(file)

        if auth['Authorization'] is not None and Token is not None:
            auth['Authorization'] = Token
        if auth['User-Agent'] is not None and GithubUsername is not None or ProjectName is not None or Email is not None:
            auth['User-Agent'] = f"{GithubUsername}/{ProjectName} ({Email})"

        with open('ModrinthAPI/auth.json', 'w') as file:
            json.dump(auth, file, indent=4)

    except FileNotFoundError:
        user_auth = None
        user_agent = None
        auth = None

        if Token is not None:
            user_auth = {'Authorization': Token}
            if GithubUsername is None and ProjectName is None and Email is None:
                auth = user_auth

        if GithubUsername is not None or ProjectName is not None or Email is not None:
            user_agent = {'User-Agent': f"{GithubUsername}/{ProjectName} ({Email})"}
            if user_auth is None:
                auth = user_agent

        if user_auth is not None and user_agent is not None:
            auth = user_auth | user_agent

        with open('ModrinthAPI/auth.json', 'w') as file:
            json.dump(auth, file, indent=4)
