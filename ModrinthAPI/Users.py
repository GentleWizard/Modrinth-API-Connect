from .utils.API_Request import request

import json

api_version = "v2"
base_url = f"https://api.modrinth.com/{api_version}"


def get(user_id: str | None = None, username: str | None = None):
    """
    The function retrieves a user's data by their ID or username and returns a dictionary of the user's data.

    ---

    ### ---Parameters---

    :param user_id: The ID of the user to retrieve
    :type user_id: str (optional)

    :param username: The username of the user to retrieve
    :type username: str (optional)

    :return: the result of a user query based on the provided parameters. The function returns a dictionary
    of user data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_user_url = f"{base_url}/user/{user_id or username}"

    # return error if no user_id or slug provided
    if user_id is None and username is None:
        return "Error: No user_id or username provided"

    # make request
    response, status_code = request(api_user_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_authenticated():
    """
    The function retrieves the authenticated user's data and returns a dictionary of the user's data.

    ---

    ### ---Parameters---

    :return: the result of a user query based on the provided parameters. The function returns a dictionary
    of user data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_user_from_auth_url = f"{base_url}/user"

    # make request
    response, status_code = request(api_user_from_auth_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    # return data
    elif response is not None:
        return response


def get_multiple(user_ids: list | None = None):
    """
    The function retrieves multiple users' data by their IDs and returns a list of dictionaries containing
    the users' data.

    ---

    ### ---Parameters---

    :param user_ids: A list of user IDs to retrieve
    :type user_ids: list (optional)

    :return: A list of dictionaries containing the users' data. Each dictionary represents a user and
    contains keys representing the user's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_users_url = f"{base_url}/users"

    # return error if no user_ids provided
    if user_ids is None:
        return "Error: No user_ids provided"

    params = {"user_ids": json.dumps(user_ids)}

    # make request
    response, status_code = request(api_multiple_users_url, params=params, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_projects(user_id: str | None = None, username: str | None = None):
    """
    The function retrieves a list of projects for a user with the given ID or username and returns a list of
    dictionaries containing the projects' data.

    ---

    ### ---Parameters---

    :param user_id: The ID of the user to retrieve projects for
    :type user_id: str (optional)

    :param username: The username of the user to retrieve projects for
    :type username: str (optional)

    :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
    contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_user_projects_url = f"{base_url}/user/{user_id or username}/projects"

    # return error if no user_id or slug provided
    if user_id is None and username is None:
        return "Error: No user_id or username provided"

    # make request
    response, status_code = request(api_user_projects_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_notifications(user_id: str | None = None, username: str | None = None):
    """
    The function retrieves a list of notifications for a user with the given ID or username and returns a
    list of dictionaries containing the notifications' data.

    ---

    ### ---Parameters---

    :param user_id: The ID of the user to retrieve notifications for
    :type user_id: str (optional)

    :param username: The username of the user to retrieve notifications for
    :type username: str (optional)

    :return: A list of dictionaries containing the notifications' data. Each dictionary represents a
    notification and contains keys representing the notification's data and their corresponding values.
    """

    # set API endpoint
    api_user_notification_url = f"{base_url}/user/{user_id or username}/notifications"

    # return error if no user_id or username provided
    if user_id is None and username is None:
        return "Error: No user_id or username provided"

    # make request
    response, status_code = request(api_user_notification_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_followed_projects(username: str | None = None, user_id: str | None = None):
    """
    The function retrieves a list of projects followed by a user with the given ID or username and returns a
    list of dictionaries containing the projects' data.

    ---

    ### ---Parameters---

    :param username: The username of the user to retrieve followed projects for
    :type username: str (optional)

    :param user_id: The ID of the user to retrieve followed projects for
    :type user_id: str (optional)

    :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
    contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_user_followed_projects_url = f"{base_url}/user/{user_id or username}/follows"

    # return error if no user_id or username provided
    if user_id is None and username is None:
        return "Error: No user_id or username provided"

    # make request
    response, status_code = request(api_user_followed_projects_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    elif isinstance(response, dict) and "projects" in response:
        # return data
        return response["projects"]

    else:
        # handle error
        return "Error: Invalid response format"


def get_payout_history(user_id: str | None = None, username: str | None = None):
    """
    The function retrieves a user's payout history by their ID or username and returns a dictionary of the
    user's payout history.

    ---

    ### ---Parameters---

    :param user_id: The ID of the user to retrieve payout history for
    :type user_id: str (optional)

    :param username: The username of the user to retrieve payout history for
    :type username: str (optional)

    :return: A dictionary of the user's payout history. The dictionary contains keys representing the payout
    history data and their corresponding values.
    """

    # set API endpoint
    api_user_payout_history_url = f"{base_url}/user/{user_id or username}/payouts"

    # return error if no user_id or username provided
    if user_id is None and username is None:
        return "Error: No user_id or username provided"

    # make request
    response, status_code = request(api_user_payout_history_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    elif response is not None:
        # return data
        return response
