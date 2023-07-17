from .utils.API_Request import request

import json

api_version = 'v2'
base_url = f'https://api.modrinth.com/{api_version}'


def search(query: str, limit: int = 5, offset: int = 0, facets: list = None):
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
    response, status_code = request(api_search_url, params=params)

    if status_code != 200:
        print(f'Error: {response}')

    elif len(response['hits']) > 0:
        # return data
        return response['hits']


def get(id: str = None, slug: str = None):
    """
        The function retrieves a project by its ID or slug and returns a dictionary of the project's data.

        ---

        ### ---Parameters---

        :param id: The ID of the project to retrieve
        :type id: str

        :param slug: The slug of the project to retrieve
        :type slug: str

        :return: the result of a project query based on the provided parameters. The function returns a
        dictionary of project data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_project_url = f'{base_url}/project/{id or slug}'

    # return error if no id or slug provided
    if id is None and slug is None:
        return "Error: No id or slug provided"

    # make request
    response, status_code = request(api_project_url)

    if status_code != 200:
        print(f'Error: {response}')

    elif response is not None:
        return response


def validate(id: str):
    """
        The function validates whether a project with the given ID exists and is accessible.

        ---

        ### ---Parameters---

        :param id: The ID of the project to validate
        :type id: str

        :return: A boolean value indicating whether the project with the given ID exists and is accessible.
    """

    # set API endpoint
    api_validity_url = f'{base_url}/project/{id}/check'

    # make request
    if id is None:
        return "Error: No id or slug provided"

    # return data
    response, status_code = request(api_validity_url)
    return response, status_code


def dependencies(id: str):
    """
        The function retrieves a list of dependencies for a project with the given ID and returns a list of
        dictionaries containing the dependencies' data.

        ---

        ### ---Parameters---

        :param id: The ID of the project to retrieve dependencies for
        :type id: str

        :return: A list of dictionaries containing the dependencies' data. Each dictionary represents a
        dependency and contains keys representing the dependency's data and their corresponding values.
        """

    # set API endpoint
    api_dependencies_url = f'{base_url}/project/{id}/dependencies'

    # return error if no id or slug provided
    if id is None:
        return "Error: No id or slug provided"

    # make request
    response, status_code = request(api_dependencies_url)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response['dependencies']


def get_multiple(ids: list):
    """
        The function retrieves multiple projects by their IDs and returns a list of dictionaries containing the
        projects' data.

        ---

        ### ---Parameters---

        :param ids: A list of project IDs to retrieve
        :type ids: list

        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_projects_url = f'{base_url}/projects'

    # return error if no id or slug provided
    if ids is None:
        return "Error: No id or slug provided"

    # params
    params = {
        'ids': json.dumps(ids)
    }

    # make request
    response, status_code = request(api_multiple_projects_url, params=params)

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

    # return error if no id or slug provided
    if count < 1:
        return "Error: Count must be greater than 0"

    # params
    params = {
        'count': count
    }

    # make request
    response, status_code = request(api_random_projects_url, params=params)

    if status_code != 200:
        print(f'Error: {response}')

    else:
        # return data
        return response


