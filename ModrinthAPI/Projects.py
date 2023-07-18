from .utils.API_Request import request

import json

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


def search(query: str,
           limit: int = 5,
           offset: int = 0,
           facets: list = None):
    """
        The function searches for data based on a query and returns a list of results.

        ---

        ### ---Parameters---

        :param query: The search query string
        :type query: str

        :param limit: The maximum number of results to return in the search query. The default value is 5,
        defaults to 5
        :type limit: int (optional)

        :param offset: The offset parameter is used to specify the starting point of the search results. It
        determines how many search results to skip before returning the desired results. For example, if
        offset is set to 10, the search results will start from the 11th result, defaults to 0
        :type offset: int (optional)

        :param facets: Facets are filters that can be applied to a search query to narrow down the results
        based on specific criteria. In this code, the `facets` parameter is a list of facets that can be
        applied to the search query. If `facets` is not None, it is converted to a
        :type facets: list

        :return: the result of a search query based on the provided parameters, including the query string,
        limit and offset values, and any specified facets. The function returns a list of results, with each
        result represented as a dictionary containing a 'slug' key and its corresponding value.
    """

    # set API endpoint
    api_search_url = f'{base_url}/search'

    # set limit and offset minimums
    limit = max(limit, 1)
    offset = max(offset, 0)

    # params
    params = {
        'query': query,
        'limit': limit,
        'offset': offset,
        'facets': json.dumps(facets) if facets is not None else None,
    }

    # make request
    response, status_code = request(api_search_url, params=params, method='GET')

    if status_code != 200:
        print(f'Error: {response}')

    elif len(response['hits']) > 0:
        # return data
        return response['hits']


def get(project_id: str = None,
        slug: str = None):
    """
        The function retrieves a project by its ID or slug and returns a dictionary of the project's data.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to retrieve
        :type project_id: str

        :param slug: The slug of the project to retrieve
        :type slug: str

        :return: the result of a project query based on the provided parameters. The function returns a
        dictionary of project data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_project_url = f'{base_url}/project/{project_id or slug}'

    # return error if no user_id or slug provided
    if project_id is None and slug is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = request(api_project_url, method='GET')

    if status_code != 200:
        print(f'Error: {response}')

    elif response is not None:
        return response


def validate(project_id: str):
    """
        The function validates whether a project with the given ID exists and is accessible.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to validate
        :type project_id: str

        :return: A boolean value indicating whether the project with the given ID exists and is accessible.
    """

    # set API endpoint
    api_validity_url = f'{base_url}/project/{project_id}/check'

    # make request
    if project_id is None:
        return "Error: No user_id or slug provided"

    # return data
    response, status_code = request(api_validity_url, method='GET')
    return response, status_code


def dependencies(project_id: str):
    """
        The function retrieves a list of dependencies for a project with the given ID and returns a list of
        dictionaries containing the dependencies' data.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to retrieve dependencies for
        :type project_id: str

        :return: A list of dictionaries containing the dependencies' data. Each dictionary represents a
        dependency and contains keys representing the dependency's data and their corresponding values.
        """

    # set API endpoint
    api_dependencies_url = f'{base_url}/project/{project_id}/dependencies'

    # return error if no user_id or slug provided
    if project_id is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = request(api_dependencies_url, method='GET')

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response['dependencies']


def get_multiple(project_ids: list):
    """
        The function retrieves multiple projects by their IDs and returns a list of dictionaries containing the
        projects' data.

        ---

        ### ---Parameters---

        :param project_ids: A list of project IDs to retrieve
        :type project_ids: list

        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_projects_url = f'{base_url}/projects'

    # return error if no user_id or slug provided
    if project_ids is None:
        return "Error: No user_id or slug provided"

    # params
    params = {
        'user_ids': json.dumps(project_ids)
    }

    # make request
    response, status_code = request(api_multiple_projects_url, params=params, method='GET')

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response['projects']


def get_random(count: int):
    """
    The function retrieves a random selection of projects and returns a list of dictionaries containing the
    projects' data.

    ---

    ### ---Parameters---

    :param count: The number of random projects to retrieve
    :type count: int

    :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
    contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_random_projects_url = f'{base_url}/projects_random'

    # return error if no user_id or slug provided
    if count < 1:
        return "Error: Count must be greater than 0"

    # params
    params = {
        'count': count
    }

    # make request
    response, status_code = request(api_random_projects_url, params=params, method='GET')

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


def edit_project(project_id: str = None,
                 slug: str = None,
                 title: str = None,
                 description: str = None,
                 categories: list[str, ...] = None,
                 client_side: str = None,
                 server_side: str = None,
                 body: str = None,
                 additional_categories: list[str, ...] = None,
                 issues_url: str = None,
                 source_url: str = None,
                 wiki_url: str = None,
                 discord_url: str = None,
                 donation_urls: list[str, ...] = None,
                 license_id: str = None,
                 status: str = None,
                 requested_status: str = None,
                 moderation_message: str = None,
                 moderation_message_body: str = None,
                 ):
    """
        The function modifies a project with the given ID and returns a dictionary containing the project's
        data.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to modify
        :type project_id: str

        :param slug: The slug of the project to modify
        :type slug: str

        :param title: The title of the project
        :type title: str

        :param description: The description of the project
        :type description: str

        :param categories: A list of categories the project belongs to
        :type categories: list[str, ...]

        :param client_side: The client-side language the project uses
        :type client_side: str

        :param server_side: The server-side language the project uses
        :type server_side: str

        :param body: The body of the project
        :type body: str

        :param additional_categories: A list of additional categories the project belongs to
        :type additional_categories: list[str, ...]

        :param issues_url: The URL to the project's issues page
        :type issues_url: str

        :param source_url: The URL to the project's source code
        :type source_url: str

        :param wiki_url: The URL to the project's wiki
        :type wiki_url: str

        :param discord_url: The URL to the project's Discord server
        :type discord_url: str

        :param donation_urls: A list of dictionaries containing the project's donation URLs
        :type donation_urls: list[str, ...]

        :param license_id: The ID of the project's license
        :type license_id: str

        :param status: The status of the project
        :type status: str

        :param requested_status: The requested status of the project
        :type requested_status: str

        :param moderation_message: The moderation message of the project
        :type moderation_message: str

        :param moderation_message_body: The moderation message body of the project
        :type moderation_message_body: str

        :return: A dictionary containing the project's data. The dictionary represents a project and contains keys
        representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_modify_project_url = f'{base_url}/project/{project_id}'

    # return error if no user_id or slug provided
    if project_id is None:
        return "Error: No user_id or slug provided"

    data = {
        'slug': slug,
        'title': title,
        'description': description,
        'categories': json.dumps(categories),
        'client_side': client_side,
        'server_side': server_side,
        'body': body,
        'additional_categories': json.dumps(additional_categories),
        'issues_url': issues_url,
        'source_url': source_url,
        'wiki_url': wiki_url,
        'discord_url': discord_url,
        'donation_urls': json.dumps(donation_urls),
        'license_id': license_id,
        'status': status,
        'requested_status': requested_status,
        'moderation_message': moderation_message,
        'moderation_message_body': moderation_message_body
    }

    # make request
    response, status_code = request(api_modify_project_url, method='Patch', data=data)

    if status_code != 204:
        print(f'Error: {response}')

    else:
        # return data
        return response


def edit_multiple_projects(project_ids: list,
                           data: dict):
    """
        The function modifies multiple projects with the given IDs and returns a list of dictionaries containing the
        projects' data.

        ---

        ### ---Parameters---

        :param project_ids: A list of project IDs to modify
        :type project_ids: list

        :param data: A dictionary of data to modify the projects with. The data must be in the form of a
        dictionary, with each key representing a piece of data and its corresponding value.
        :type data: dict

        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_modify_multiple_projects_url = f'{base_url}/projects'

    # return error if no user_id or slug provided
    if project_ids is None:
        return "Error: No user_id or slug provided"

    # params
    params = {
        'user_ids': json.dumps(project_ids)
    }

    # make request
    response, status_code = request(api_modify_multiple_projects_url, params=params, method='Patch', data=data)

    if status_code != 204:
        print(f'Error: {response}')

    else:
        # return data
        return response


def edit_project_icon(project_id: str,
                      icon: str,
                      slug: str = None):
    """
        The function modifies a project's icon with the given ID and returns a dictionary containing the project's
        data.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to modify
        :type project_id: str

        :param icon: The icon to set the project to
        :type icon: str

        :param slug: The slug of the project to modify
        :type slug: str

        :return: A dictionary containing the project's data. The dictionary represents the project and contains
        keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_modify_project_icon_url = f'{base_url}/project/{project_id or slug}/icon'

    # return error if no user_id or slug provided
    if project_id is None:
        return "Error: No user_id or slug provided"

    # get image
    path = icon
    with open(path, 'rb') as f:
        image_data = f.read()

    # params
    files = {
        'icon': image_data
    }

    # make request
    response, status_code = request(api_modify_project_icon_url, files=files, method='Patch')

    if status_code != 204:
        print(f'Error: {response}')

    else:
        # return data
        return response


def edit_gallery_image(project_id: str,
                       url: str,
                       slug: str = None,
                       featured: bool = False,
                       title: str = None,
                       description: str = None,
                       ordering: int = None):
    """
        The function modifies a project's gallery image with the given ID and returns a dictionary containing the
        project's data.

        ---

        ### ---Parameters---

        :param project_id: The ID of the project to modify
        :type project_id: str

        :param slug: The slug of the project to modify
        :type slug: str

        :param url: The URL of the image to set the project to
        :type url: str

        :param featured: Whether the image should be featured
        :type featured: bool

        :param title: The title of the image
        :type title: str

        :param description: The description of the image
        :type description: str

        :param ordering: The ordering of the image
        :type ordering: int

        :return: A dictionary containing the project's data. The dictionary represents the project and contains
        keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_modify_gallery_image_url = f'{base_url}/project/{project_id or slug}/gallery'

    # return error if no user_id or slug provided
    if project_id is None:
        return "Error: No user_id or slug provided"

    # data
    data = {
        'url': url,
        'featured': featured,
        'title': title,
        'description': description,
        'ordering': ordering
    }
    # make request
    response, status_code = request(api_modify_gallery_image_url, data=data, method='Patch')

    if status_code != 204:
        print(f'Error: {response}')

    else:
        # return data
        return response
