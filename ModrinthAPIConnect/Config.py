All_Auth = None

def set_Auth(Token: str = None, GithubUsername: str = None, ProjectName: str = None, Email: str = None):
    global All_Auth
    # set authentication
    User_Auth = {'Authorization': Token}

    # set user agent
    User_Agent = {'User-Agent': f"{GithubUsername}/{ProjectName} ({Email})"}

    # combine headers
    All_Auth = User_Auth | User_Agent
    

def return_Auth():
    return All_Auth
