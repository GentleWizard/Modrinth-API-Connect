from .utils.API_Request_Async import request_async as request

import json
import asyncio

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


async def get(id: str = None, username: str = None):
    """
        The function retrieves a user's data by their ID or username and returns a dictionary of the user's data.

        ---

        ### ---Parameters---

        :param id: The ID of the user to retrieve
        :type id: str (optional)

        :param username: The username of the user to retrieve
        :type username: str (optional)

        :return: the result of a user query based on the provided parameters. The function returns a dictionary
        of user data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_user_url = f'{base_url}/user/{id or username}'

    # return error if no id or slug provided
    if id is None and username is None:
        return "Error: No id or username provided"

    # make request
    response, status_code = await request(api_user_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_authenticated():
    """
        The function retrieves the authenticated user's data and returns a dictionary of the user's data.

        ---

        ### ---Parameters---

        :return: the result of a user query based on the provided parameters. The function returns a dictionary
        of user data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_user_from_auth_url = f'{base_url}/user'

    # make request
    response, status_code = await request(api_user_from_auth_url)

    if status_code != 200:
        print(f'Error: {response}')

    # return data
    elif response is not None:
        return response


async def get_multiple(ids: list = None):
    """
        The function retrieves multiple users' data by their IDs and returns a list of dictionaries containing
        the users' data.

        ---

        ### ---Parameters---

        :param ids: A list of user IDs to retrieve
        :type ids: list (optional)

        :return: A list of dictionaries containing the users' data. Each dictionary represents a user and
        contains keys representing the user's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_users_url = f'{base_url}/users'

    # return error if no ids provided
    if ids is None:
        return "Error: No ids provided"

    params = {
        'ids': json.dumps(ids)
    }

    # make request
    response, status_code = await request(api_multiple_users_url, params=params)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_projects(id: str = None, username: str = None):
    """
        The function retrieves a list of projects for a user with the given ID or username and returns a list of
        dictionaries containing the projects' data.

        ---

        ### ---Parameters---

        :param id: The ID of the user to retrieve projects for
        :type id: str (optional)

        :param username: The username of the user to retrieve projects for
        :type username: str (optional)

        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_user_projects_url = f'{base_url}/user/{id or username}/projects'

    # return error if no id or slug provided
    if id is None and username is None:
        return "Error: No id or username provided"

    # make request
    response, status_code = await request(api_user_projects_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_notifications(id: str = None, username: str = None):
    """
        The function retrieves a list of notifications for a user with the given ID or username and returns a
        list of dictionaries containing the notifications' data.

        ---

        ### ---Parameters---

        :param id: The ID of the user to retrieve notifications for
        :type id: str (optional)

        :param username: The username of the user to retrieve notifications for
        :type username: str (optional)

        :return: A list of dictionaries containing the notifications' data. Each dictionary represents a
        notification and contains keys representing the notification's data and their corresponding values.
    """

    # set API endpoint
    api_user_notification_url = f'{base_url}/user/{id or username}/notifications'

    # return error if no id or username provided
    if id is None and username is None:
        return "Error: No id or username provided"

    # make request
    response, status_code = await request(api_user_notification_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_followed_projects(username: str = None, id: str = None):
    """
        The function retrieves a list of projects followed by a user with the given ID or username and returns a
        list of dictionaries containing the projects' data.

        ---

        ### ---Parameters---

        :param username: The username of the user to retrieve followed projects for
        :type username: str (optional)

        :param id: The ID of the user to retrieve followed projects for
        :type id: str (optional)

        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_user_followed_projects_url = f'{base_url}/user/{id or username}/follows'

    # return error if no id or username provided
    if id is None and username is None:
        return "Error: No id or username provided"

    # make request
    response, status_code = await request(api_user_followed_projects_url)

    if status_code != 200:
        print(f'Error: {response}')

    elif response is not None:
        # return data
        return response['projects']


async def get_payout_history(id: str = None, username: str = None):
    """
    The function retrieves a user's payout history by their ID or username and returns a dictionary of the
    user's payout history.

    ---

    ### ---Parameters---

    :param id: The ID of the user to retrieve payout history for
    :type id: str (optional)

    :param username: The username of the user to retrieve payout history for
    :type username: str (optional)

    :return: A dictionary of the user's payout history. The dictionary contains keys representing the payout
    history data and their corresponding values.
    """

    # set API endpoint
    api_user_payout_history_url = f'{base_url}/user/{id or username}/payouts'

    # return error if no id or username provided
    if id is None and username is None:
        return "Error: No id or username provided"

    # make request
    response, status_code = await request(api_user_payout_history_url)

    if status_code != 200:
        print(f'Error: {response}')

    elif response is not None:
        # return data
        return response
