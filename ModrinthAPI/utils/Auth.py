import json


def set_auth(
    token: str | None = None,
    github_username: str | None = None,
    project_name: str | None = None,
    email: str | None = None,
):
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
        with open("ModrinthAPI/auth.json", "r", encoding="utf-8") as file:
            auth = json.load(file)

        if auth["Authorization"] is not None and token is not None:
            auth["Authorization"] = token
        if (
            auth["User-Agent"] is not None
            and github_username is not None
            or project_name is not None
            or email is not None
        ):
            auth["User-Agent"] = f"{github_username}/{project_name} ({email})"

        with open("ModrinthAPI/auth.json", "w", encoding="utf-8") as file:
            json.dump(auth, file, indent=4)

    except FileNotFoundError:
        create_auth_file(token, github_username, project_name, email)


def create_auth_file(token, github_username, project_name, email):
    """
    The function creates an auth.json file with the given token, GitHub username, project name, and email.

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
    user_auth = None
    user_agent = None
    auth = None

    if token is not None:
        user_auth = {"Authorization": token}
        if github_username is None and project_name is None and email is None:
            auth = user_auth

    if github_username is not None or project_name is not None or email is not None:
        user_agent = {"User-Agent": f"{github_username}/{project_name} ({email})"}
        if user_auth is None:
            auth = user_agent

    if user_auth is not None and user_agent is not None:
        auth = user_auth | user_agent

    with open("ModrinthAPI/auth.json", "w", encoding="utf-8") as file:
        json.dump(auth, file, indent=4)
