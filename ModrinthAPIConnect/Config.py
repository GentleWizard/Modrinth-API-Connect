All_Auth = None

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
    

def return_Auth():
    """
    The function returns the authentication and user agent headers for API requests as a dictionary.
    
    ---
    
    ### ---Parameters---
    
    :return: A dictionary containing the authentication and user agent headers for API requests.
    """
    return All_Auth
