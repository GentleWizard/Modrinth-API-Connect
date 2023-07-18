auth = {}


def set_auth(Token: str = None, GithubUsername: str = None, ProjectName: str = None, Email: str = None):
    """
    The function sets the authentication and user agent headers for API requests. It takes in a token, Github
    username, project name, and email as parameters and combines them into a dictionary of headers.

    ---

    ### ---Parameters---

    :param Token: The authentication token to be used in API requests (HIGHLY RECOMMENDED TO USE A CSV FILE TO STORE TOKENS)
    :type Token: str (optional)

    :param GithubUsername: The GitHub username to be used in the user agent header of API requests
    :type GithubUsername: str (optional)

    :param ProjectName: The project name to be used in the user agent header of API requests
    :type ProjectName: str (optional)

    :param Email: The email to be used in the user agent header of API requests
    :type Email: str (optional)

    :return: None
    """

    global auth
    # set authentication
    user_auth = {'Authorization': Token}
    # set user agent
    user_agent = {'User-Agent': f"{GithubUsername}/{ProjectName} ({Email})"}
    # combine headers
    All_Auth = user_auth | user_agent
