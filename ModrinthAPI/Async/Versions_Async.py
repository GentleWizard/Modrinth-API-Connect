from .utils.API_Request_Async import request_async as request

import json
import asyncio

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


async def get(id: str):
    """
        The function retrieves a version of a project by its ID and returns a dictionary of the version's data.

        ---

        ### ---Parameters---

        :param id: The ID of the version to retrieve
        :type id: str

        :return: the result of a version query based on the provided parameters. The function returns a
        dictionary of version data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_version_url = f'{base_url}/version/{id}'

    # return error if no user_id or slug provided
    if id is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = await request(api_version_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_list(id: str, loaders: list = None, game_versions: list = None,
                   featured: bool = False):
    """
        The function retrieves a list of versions for a project with the given ID and returns a list of
        dictionaries containing the versions' data.

        ---

        ### ---Parameters---

        :param id: The ID of the project to retrieve versions for
        :type id: str

        :param loaders: A list of loaders to filter the versions by
        :type loaders: list (optional)

        :param game_versions: A list of game versions to filter the versions by
        :type game_versions: list (optional)

        :param featured: A boolean parameter that determines whether to only return featured versions or not.
        If set to True, only featured versions will be returned. If set to False, all versions will be returned.
        Defaults to False
        :type featured: bool (optional)

        :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
        contains keys representing the version's data and their corresponding values.
    """

    # set API endpoint
    api_list_version_url = f'{base_url}/project/{id}/version'

    # params
    params = {
        'loaders': json.dumps(loaders),
        'game_versions': json.dumps(game_versions),
        'featured': 'true' if featured else 'false',
    }

    # return error if no user_id or slug provided
    if id is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = await request(api_list_version_url, params=params)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_multiple(ids: list):
    """
        The function retrieves multiple versions of a project by their IDs and returns a list of dictionaries
        containing the versions' data.

        ---

        ### ---Parameters---

        :param ids: A list of version IDs to retrieve
        :type ids: list

        :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
        contains keys representing the version's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_versions_url = f'{base_url}/versions'

    # return error if no user_id or slug provided
    if ids is None:
        return "Error: No user_id or slug provided"

    # params
    params = {
        'user_ids': json.dumps(ids)
    }

    # make request
    response, status_code = await request(api_multiple_versions_url, params=params)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


async def get_from_hash(hash: str):
    """
        The function retrieves a version of a project by its version_hash and returns a dictionary of the version's data.

        ---

        ### ---Parameters---

        :param hash: The version_hash of the version to retrieve
        :type hash: str

        :return: the result of a version query based on the provided parameters. The function returns a
        dictionary of version data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_project_versions_hash_url = f'{base_url}/version_file/{hash}'

    # return error if no user_id or slug provided
    if hash is None:
        return "Error: No version_hash provided"

    # make request
    response, status_code = await request(api_project_versions_hash_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response
