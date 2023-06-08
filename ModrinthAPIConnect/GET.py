"""
Status: In development

---

Gets data from the Modrinth API and puts it into a dictionary to be used in your code.
"""

from ModrinthAPIConnect.utils.Request import Request
from ModrinthAPIConnect.utils.SortData import dict_result, list_result

import json
import requests
import concurrent.futures



# ModrinthAPI GET class
class Project:
    """
    The `Project` class represents the project endpoint of the Modrinth API. It contains the API version, base
    URL, search parameters, limit, and offset for the API requests to the project endpoint.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the `Project` class with the API version, base URL, search parameters,
        limit, and offset for the API requests to the project endpoint.
        """
        self.api_version = 'v2'
        self.base_url = f'https://api.modrinth.com/{self.api_version}/project'
        self.search_params = {}
        self.limit = 1
        self.offset = 0


    def search(self, query: str, limit: int = 5, offset: int = 0, data: list = None, facets: list = None, async_: bool = False):
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
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param facets: Facets are filters that can be applied to a search query to narrow down the results
        based on specific criteria. In this code, the `facets` parameter is a list of facets that can be
        applied to the search query. If `facets` is not None, it is converted to a
        :type facets: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a search query based on the provided parameters, including the query string,
        limit and offset values, and any specified facets. The function returns a list of results, with each
        result represented as a dictionary containing a 'slug' key and its corresponding value.
        """

        # set API endpoint
        self.api_search_url = f'{self.base_url}/search'

        # set limit and offset minimums
        self.limit = max(self.limit, 1)
        self.offset = max(self.offset, 0)

        # params
        params = {
            'query': query,
            'limit': limit,
            'offset': offset,
            'facets': json.dumps(facets) if facets is not None else None,
        }

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_search_url, params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_search_url, params=params)

        if status_code != 200:
            print(f'Error: {response}')

        elif len(response['hits']) > 0:
            # return data
            return list_result('slug', data, response['hits'])

    def get(self, id: str = None, slug: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a project by its ID or slug and returns a dictionary of the project's data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the project to retrieve
        :type id: str
        
        :param slug: The slug of the project to retrieve
        :type slug: str
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a project query based on the provided parameters. The function returns a
        dictionary of project data, with each key representing a piece of data and its corresponding value.
        """

        # set API endpoint
        self.api_project_url = f'{self.base_url}/project/{id or slug}'

        # return error if no id or slug provided
        if id is None and slug is None:
            return "Error: No id or slug provided"

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_project_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_project_url)

        if status_code != 200:
            print(f'Error: {response}')

        elif response is not None:
            return dict_result('id', data, response)

    def validate(self, id: str):
        """
        The function validates whether a project with the given ID exists and is accessible.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the project to validate
        :type id: str
        
        :return: A boolean value indicating whether the project with the given ID exists and is accessible.
        """


        # set API endpoint
        self.api_validity_url = f'{self.base_url}/project/{id}/check'

        # make request
        if id is None:
            return "Error: No id or slug provided"

        # return data
        response = requests.get(self.api_validity_url, timeout=10)
        return response.status_code == 200

    def dependencies(self, id: str, data: list = None, async_: bool = False):
        """
        The function retrieves a list of dependencies for a project with the given ID and returns a list of
        dictionaries containing the dependencies' data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the project to retrieve dependencies for
        :type id: str
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the dependencies' data. Each dictionary represents a
        dependency and contains keys representing the dependency's data and their corresponding values.
        """

        # set API endpoint
        self.api_dependencies_url = f'{self.base_url}/project/{id}/dependencies'

        # return error if no id or slug provided
        if id is None:
            return "Error: No id or slug provided"

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_dependencies_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_dependencies_url)            

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('slug', data, response['projects'])

    def get_Multiple(self, ids: list, data: list = None, async_: bool = False):
        """
        The function retrieves multiple projects by their IDs and returns a list of dictionaries containing the
        projects' data.
        
        ---
        
        ### ---Parameters---
        
        :param ids: A list of project IDs to retrieve
        :type ids: list
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
        """


        # set API endpoint
        self.api_multiple_projects_url = f'{self.base_url}/projects'

        # return error if no id or slug provided
        if ids is None:
            return "Error: No id or slug provided"

        # params
        params = {
            'ids': json.dumps(ids)
        }

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_multiple_projects_url, params=params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_multiple_projects_url, params=params)          

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('slug', data, response)

    def get_Random(self, count: int, data: list = None, async_: bool = False):
        """
        The function retrieves a random selection of projects and returns a list of dictionaries containing the
        projects' data.
        
        ---
        
        ### ---Parameters---
        
        :param count: The number of random projects to retrieve
        :type count: int
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
        """

        # set API endpoint
        self.api_random_projects_url = f'{self.base_url}/projects_random'

        # return error if no id or slug provided
        if count < 1:
            return "Error: Count must be greater than 0"

        # params
        params = {
            'count': count
        }

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_random_projects_url, params=params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_random_projects_url, params=params)          
        

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('slug', data, response)


class Version:
    """
    The `Version` class represents the version endpoint of the Modrinth API being used. It contains the API
    version and base URL for the API requests to the version endpoint.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the `Version` class with the API version and base URL for the API
        requests to the version endpoint.
        """
        self.api_version = 'v2'
        self.base_url = f'https://api.modrinth.com/{self.api_version}/version'

    def get(self, id: str, data: list = None, async_: bool = False):
        """
        The function retrieves a version of a project by its ID and returns a dictionary of the version's data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the version to retrieve
        :type id: str
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a version query based on the provided parameters. The function returns a
        dictionary of version data, with each key representing a piece of data and its corresponding value.
        """


        # set API endpoint
        self.api_version_url = f'{self.base_url}/version/{id}'

        # return error if no id or slug provided
        if id is None:
            return "Error: No id or slug provided"

        # make request
        response, status_code = Request(url=self.api_version_url)
        
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_version_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_version_url)     

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return dict_result('name', data, response)

    def get_List(self, id: str, data: list = None, loaders: list = None, game_versions: list = None, featured: bool = False, async_: bool = False):
        """
        The function retrieves a list of versions for a project with the given ID and returns a list of
        dictionaries containing the versions' data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the project to retrieve versions for
        :type id: str
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param loaders: A list of loaders to filter the versions by
        :type loaders: list (optional)
        
        :param game_versions: A list of game versions to filter the versions by
        :type game_versions: list (optional)
        
        :param featured: A boolean parameter that determines whether to only return featured versions or not.
        If set to True, only featured versions will be returned. If set to False, all versions will be returned.
        Defaults to False
        :type featured: bool (optional)
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
        contains keys representing the version's data and their corresponding values.
        """
        

        # set API endpoint
        self.api_list_version_url = f'{self.base_url}/project/{id}/version'

        # params
        params = {
            'loaders': json.dumps(loaders),
            'game_versions': json.dumps(game_versions),
            'featured': 'true' if featured else 'false',
        }

        # return error if no id or slug provided
        if id is None:
            return "Error: No id or slug provided"

        # make request        
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_list_version_url, params=params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_list_version_url, params=params)     

        if status_code != 200:
            print(f'Error: {response}')
            
        else:
            # return data
            return list_result('id', data, response)

    def get_Multiple(self, ids: list, data: list = None, async_: bool = False):
        """
        The function retrieves multiple versions of a project by their IDs and returns a list of dictionaries
        containing the versions' data.
        
        ---
        
        ### ---Parameters---
        
        :param ids: A list of version IDs to retrieve
        :type ids: list
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
        contains keys representing the version's data and their corresponding values.
        """


        # set API endpoint
        self.api_multiple_versions_url = f'{self.base_url}/versions'

        # return error if no id or slug provided
        if ids is None:
            return "Error: No id or slug provided"

        # params
        params = {
            'ids': json.dumps(ids)
        }

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_multiple_versions_url, params=params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_multiple_versions_url, params=params)    

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('name', data, response)

    def get_From_Hash(self, hash: str, data: list = None, async_: bool = False):
        """
        The function retrieves a version of a project by its hash and returns a dictionary of the version's data.
        
        ---
        
        ### ---Parameters---
        
        :param hash: The hash of the version to retrieve
        :type hash: str
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a version query based on the provided parameters. The function returns a
        dictionary of version data, with each key representing a piece of data and its corresponding value.
        """


        # set API endpoint
        self.api_project_versions_hash_url = f'{self.base_url}/version_file/{hash}'

        # return error if no id or slug provided
        if hash is None:
            return "Error: No hash provided"

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_project_versions_hash_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_project_versions_hash_url)     

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return dict_result('name', data, response)


class User:
    """
    The `User` class represents the user endpoint of the Modrinth API. It contains the API version and base URL
    for the API requests to the user endpoint.
    """

    def __init__(self):
        """
        Initializes a new instance of the `User` class with the API version and base URL for the API requests
        to the user endpoint.
        """
        self.api_version = 'v2'
        self.base_url = f'https://api.modrinth.com/{self.api_version}/user'

    def get(self, id: str = None, username: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a user's data by their ID or username and returns a dictionary of the user's data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the user to retrieve
        :type id: str (optional)
        
        :param username: The username of the user to retrieve
        :type username: str (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a user query based on the provided parameters. The function returns a dictionary
        of user data, with each key representing a piece of data and its corresponding value.
        """


        # set API endpoint
        self.api_user_url = f'{self.base_url}/user/{id or username}'

        # return error if no id or slug provided
        if id is None and username is None:
            return "Error: No id or username provided"

        # make request 
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_url)     

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return dict_result('username', data, response)

    def get_Authenticated(self, data: list = None, async_: bool = False):
        """
        The function retrieves the authenticated user's data and returns a dictionary of the user's data.
        
        ---
        
        ### ---Parameters---
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: the result of a user query based on the provided parameters. The function returns a dictionary
        of user data, with each key representing a piece of data and its corresponding value.
        """


        # set API endpoint
        self.api_user_from_auth_url = f'{self.base_url}/user'

        # make request
        response, status_code = Request(url=self.api_user_from_auth_url)
        
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_from_auth_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_from_auth_url)  

        if status_code != 200:
            print(f'Error: {response}')

        # return data
        elif response is not None:
            return dict_result('username', data, response)

    def get_Multiple(self, ids: list = None, data: list = None, async_: bool = False):
        """
        The function retrieves multiple users' data by their IDs and returns a list of dictionaries containing
        the users' data.
        
        ---
        
        ### ---Parameters---
        
        :param ids: A list of user IDs to retrieve
        :type ids: list (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the users' data. Each dictionary represents a user and
        contains keys representing the user's data and their corresponding values.
        """


        # set API endpoint
        self.api_multiple_users_url = f'{self.base_url}/users'

        # return error if no ids provided
        if ids is None:
            return "Error: No ids provided"

        params = {
            'ids': json.dumps(ids)
        }

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_multiple_users_url, params=params)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_multiple_users_url, params=params)

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('username', data, response)

    def get_Projects(self, id: str = None, username: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a list of projects for a user with the given ID or username and returns a list of
        dictionaries containing the projects' data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the user to retrieve projects for
        :type id: str (optional)
        
        :param username: The username of the user to retrieve projects for
        :type username: str (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
        """


        # set API endpoint
        self.api_user_projects_url = f'{self.base_url}/user/{id or username}/projects'

        # return error if no id or slug provided
        if id is None and username is None:
            return "Error: No id or username provided"

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_projects_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_projects_url)     

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('slug', data, response)

    def get_Notifications(self, id: str = None, username: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a list of notifications for a user with the given ID or username and returns a
        list of dictionaries containing the notifications' data.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the user to retrieve notifications for
        :type id: str (optional)
        
        :param username: The username of the user to retrieve notifications for
        :type username: str (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the notifications' data. Each dictionary represents a
        notification and contains keys representing the notification's data and their corresponding values.
        """


        # set API endpoint
        self.api_user_nofiications_url = f'{self.base_url}/user/{id or username}/notifications'

        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"

        # make request
        response, status_code = Request(url=self.api_user_nofiications_url)
        
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_nofiications_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_nofiications_url)     

        if status_code != 200:
            print(f'Error: {response}')

        else:
            # return data
            return list_result('id', data, response)

    def get_Followed_Projects(self, username: str = None, id: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a list of projects followed by a user with the given ID or username and returns a
        list of dictionaries containing the projects' data.
        
        ---
        
        ### ---Parameters---
        
        :param username: The username of the user to retrieve followed projects for
        :type username: str (optional)
        
        :param id: The ID of the user to retrieve followed projects for
        :type id: str (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `list_result` function to return a list of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A list of dictionaries containing the projects' data. Each dictionary represents a project and
        contains keys representing the project's data and their corresponding values.
        """

        # set API endpoint
        self.api_user_followed_projects_url = f'{self.base_url}/user/{id or username}/follows'

        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"

        # make request
        response, status_code = Request(
            url=self.api_user_followed_projects_url)
        
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_followed_projects_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_followed_projects_url)     

        if status_code != 200:
            print(f'Error: {response}')

        elif response is not None:
            # return data
            return list_result('slug', data, response)

    def get_Payout_History(self, id: str = None, username: str = None, data: list = None, async_: bool = False):
        """
        The function retrieves a user's payout history by their ID or username and returns a dictionary of the
        user's payout history.
        
        ---
        
        ### ---Parameters---
        
        :param id: The ID of the user to retrieve payout history for
        :type id: str (optional)
        
        :param username: The username of the user to retrieve payout history for
        :type username: str (optional)
        
        :param data: The `data` parameter is a list that contains the data to be searched. It is used in
        conjunction with the `dict_result` function to return a dictionary of matching results
        :type data: list
        
        :param async_: A boolean parameter that determines whether the search request should be made
        asynchronously or not. If set to True, the search request will be made using a ThreadPoolExecutor to
        run the request in a separate thread. If set to False, the search request will be made
        synchronously, defaults to False
        :type async_: bool (optional)
        
        :return: A dictionary of the user's payout history. The dictionary contains keys representing the payout
        history data and their corresponding values.
        """

        # set API endpoint
        self.api_user_payout_history_url = f'{self.base_url}/user/{id or username}/payouts'

        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"

        # make request
        if async_:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(Request, self.api_user_payout_history_url)
                response, status_code = future.result()
        else:
            response, status_code = Request(url=self.api_user_payout_history_url)     

        if status_code != 200:
            print(f'Error: {response}')

        elif response is not None:
            # return data
            return dict_result('all_time', data, response)
