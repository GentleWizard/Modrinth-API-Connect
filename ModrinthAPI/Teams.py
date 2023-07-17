from .utils.API_Request import request

import json

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


def get_project_members(project_id: str = None,
                        slug: str = None):
    """
    The function retrieves a list of members in a project's team and returns a list of dictionaries
    containing the members' data.

    ---

    ### ---Parameters---

    :param project_id: The ID of the project to retrieve team members for
    :type project_id: str

    :param slug: The slug of the project to retrieve team members for
    :type slug: str

    :return: A list of dictionaries containing the members' data. Each dictionary represents a member and
    contains keys representing the member's data and their corresponding values.
    """

    # set API endpoint
    api_project_team_members_url = f'{base_url}/project/{project_id or slug}/members'

    # make request
    response, status_code = request(api_project_team_members_url, method='GET')

    if status_code != 200:
        print(f'Error: {response}')
    else:
        # return data
        return response


def get_team_members(team_id: str = None):
    """
    The function retrieves a list of members in a team and returns a list of dictionaries
    containing the members' data.

    ---

    ### ---Parameters---

    :param team_id: The ID of the team to retrieve members for
    :type team_id: str

    :return: A list of dictionaries containing the members' data. Each dictionary represents a member and
    contains keys representing the member's data and their corresponding values.
    """

    # set API endpoint
    api_team_members_url = f'{base_url}/team/{team_id}/members'

    # make request
    response, status_code = request(api_team_members_url, method='GET')

    if status_code != 200:
        print(f'Error: {response}')
    else:
        # return data
        return response


def get_members_from_teams(team_ids: list):
    """
    The function retrieves a list of members in a team and returns a list of dictionaries
    containing the members' data.

    ---

    ### ---Parameters---

    :param team_ids: The IDs of the teams to retrieve members for
    :type team_ids: str

    :return: A list of dictionaries containing the members' data. Each dictionary represents a member and
    contains keys representing the member's data and their corresponding values.
    """

    # set API endpoint
    api_team_members_url = f'{base_url}/team/{team_ids}/members'

    # make request
    response, status_code = request(api_team_members_url, method='GET')

    if status_code != 200:
        print(f'Error: {response}')
    else:
        # return data
        return response
