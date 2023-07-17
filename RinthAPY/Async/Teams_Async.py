from .utils.API_Request_Async import request_async as request

import json
import asyncio

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


async def get_project_members(id: str = None, slug: str = None):
    """
    The function retrieves a list of members in a project's team and returns a list of dictionaries
    containing the members' data.

    ---

    ### ---Parameters---

    :param id: The ID of the project to retrieve team members for
    :type id: str

    :param slug: The slug of the project to retrieve team members for
    :type slug: str

    :return: A list of dictionaries containing the members' data. Each dictionary represents a member and
    contains keys representing the member's data and their corresponding values.
    """

    # set API endpoint
    api_project_team_members_url = f'{base_url}/project/{id or slug}/members'

    # make request
    response, status_code = await request(api_project_team_members_url)

    if status_code != 200:
        print(f'Error: {response}')
    else:
        # return data
        return response
