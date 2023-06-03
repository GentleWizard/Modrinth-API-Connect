"""
Author: GentleWizard

Github: https://github.com/GentleWizard/Modrinth-API-Connect

Description: The ModrinthAPIConnect module is a Python module that allows for interaction to and from the Modrinth v2 API

License: MIT
"""

import requests
import json


# ModrinthAPI GET class
class GET():
    def __init__(self, Token: str = None, GithubUsername: str = None, ProjectName: str = None, Email: str = None):
        """
        This is a Python class constructor that sets up authentication and user agent headers for API
        requests to Modrinth.
        
        :param Token: This is a required parameter that represents the authentication token for the Modrinth
        API. It is used to authenticate the user and allow access to the API's resources
        :type Token: str
        
        :param GithubUsername: The username of the GitHub account associated with the project that will be
        using this API
        :type GithubUsername: str
        
        :param ProjectName: The name of the project that is using this API
        :type ProjectName: str
        
        :param Email: The email address associated with the Github account being used for authentication
        :type Email: str
        """
        self.base_url = 'https://api.modrinth.com/'
        self.api_version = 'v2'
        self.search_params = {}
        self.limit = 1
        self.offset = 0
        self.token = Token

        # set authentication
        self.User_Auth = {'Authorization': self.token}

        # set user agent
        self.User_Agent = {'User-Agent': f"{GithubUsername}/{ProjectName} ({Email})"}

        # combine headers
        self.All_Auth = {**self.User_Auth, **self.User_Agent}
  
  
    def __dict_result(self, omit, data, project_data):
        """
        This function creates a dictionary with data from a project, omitting a specified item.
        
        :param omit: a string representing the key that should be omitted from the resulting dictionary
        
        :param data: This parameter is a list of keys that should be included in the resulting dictionary.
        If it is None, then all keys in the project_data dictionary should be included except for the key
        specified in the omit parameter
        
        :param project_data: a dictionary containing data for a project
        
        :return: a dictionary with a single key-value pair. The key is the value of the `omit` parameter in
        the `project_data` dictionary, and the value is a dictionary containing all the key-value pairs from
        the `project_data` dictionary except for the key-value pair with the key equal to the `omit`
        parameter. If the `data` parameter is not `None`, only
        """
        hit = project_data
        data_dict = {}
        if data is not None:
            for item in data:
                if item != omit:
                    key = item
                    value = hit.get(item, None)
                    data_dict[key] = value
        else:
            for key, value in hit.items():
                if key != omit:
                    data_dict[key] = value        
        return {hit[omit]: data_dict}
        
    def __list_result(self, omit, data, project_data):
        """
        This is a Python function that creates a dictionary of data from a list of dictionaries, excluding a
        specified key.
        
        :param omit: The parameter "omit" is a string representing the key that should be omitted from the
        dictionary values in the result
        
        :param data: A list of strings representing the keys of the dictionary that we want to extract from
        each hit in project_data. If data is None, then all keys in each hit will be extracted except for
        the key specified in the omit parameter
        
        :param project_data: a list of dictionaries containing project data
        
        :return: a dictionary where the keys are the values of the `omit` parameter in the `project_data`
        list, and the values are dictionaries containing the data from the `data` parameter (excluding the
        `omit` key) for each item in the `project_data` list. If the `data` parameter is `None`, then all
        keys and values from each item in the `
        """
        result = {}
        for dict in project_data:
            data_dict = {}
            if data is not None:
                for item in data:
                    if omit is not None and item != omit:
                        key = item
                        value = dict.get(item, None)
                        data_dict[key] = value
            if omit is not None:
                result[dict[omit]] = data_dict
            else:
                result = data_dict
        return result

    def __api_request(self, url, params: str = ""):
        """
        This is a Python function that sends an API request with specified parameters and headers, and
        returns the response data in JSON format or an error message if the request fails.
        
        :param url: The URL of the API endpoint that you want to make a request to
        
        :param params: params is a dictionary or a string that contains the query parameters to be sent with
        the API request. These parameters are used to filter or modify the response data returned by the
        API. If params is None, then no query parameters will be sent with the request
        :type params: str
        
        :return: either the project data in JSON format or an error message if there was an exception raised
        during the API request.
        """
        try:
            response = requests.get(url, params=params, headers=self.All_Auth, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(err)

            
    def search(self, query: str, limit: int=1, offset: int=0, data: list = None, facets: list = None):
        """
        This function searches for data based on a query, limit, offset, and facets, and returns a list of
        results.
        
        :param query: A string representing the search query to be executed
        :type query: str
        
        :param limit: The maximum number of results to return in the search query. The default value is 1,
        defaults to 1
        :type limit: int (optional)
        
        :param offset: The offset parameter is used to specify the starting point of the search results. It
        determines how many search results to skip before returning the results. For example, if offset is
        set to 10, the search results will start from the 11th result, defaults to 0
        :type offset: int (optional)
        
        :param data: The `data` parameter is a list that contains the fields of the search results that
        should be returned. The default value is `[None, ...]`, which means that all fields will be
        returned. If you want to specify which fields to return, you can pass a list of field names as the
        :type data: list
        
        :param facets: Facets are filters that can be applied to a search query to narrow down the results
        based on specific criteria. In this function, the facets parameter is a list of facets to be applied
        to the search query. If no facets are provided, it defaults to None
        :type facets: list
        
        :return: either "No results found" if there are no hits in the project data, or it returns a list of
        results based on the 'slug' key in the data parameter and the 'hits' key in the project data.
        """

        
        # set API endpoint        
        self.api_search_url = f'{self.base_url}{self.api_version}/search'

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
        project_data = self.__api_request(url=self.api_search_url, params=params)

        # return error if no results found
        if len(project_data['hits']) == 0:
            return "No results found"

        # return data
        return self.__list_result('slug', data, project_data['hits'])

    def project(self, id: str = None, slug: str = None, data: list = None):
        """
        This function takes an ID and optional data list, makes an API request to retrieve project data, and
        returns the project data with the specified slug.
        
        :param id: A string representing the ID of a project
        :type id: str
        
        :param data: The `data` parameter is a list that contains the specific fields or attributes of the
        project that the user wants to retrieve. If `data` is not provided, the function will return all
        available data for the project
        :type data: list
        
        :return: the result of a request to the API endpoint for a specific project, using the provided
        project ID. If no ID is provided, an error message is returned. The function also takes an optional
        parameter `data`, which is used to filter the returned data by a specific field. The function
        returns the filtered data as a dictionary.
        """

        # set API endpoint
        self.api_project_url = f'{self.base_url}{self.api_version}/project/{id or slug}'
        
        # return error if no id or slug provided
        if id is None and slug is None:
            return "Error: No id or slug provided"
        
        # make request
        project_data = self.__api_request(url=self.api_project_url)

        # return data
        if project_data is not None:
            return self.__dict_result('id', data, project_data)
            
    def validate_Project(self, id: str):
        """
        This function validates a project ID by making a request to an API endpoint and returning a boolean
        indicating whether the response status code is 200.
        
        :param id: The "id" parameter is a string that represents the unique identifier of a project. It is
        used to validate the project's existence by making a request to the API endpoint
        :type id: str
        
        :return: a boolean value indicating whether the response status code is equal to 200 or not.
        """
        
        # set API endpoint
        self.api_validity_url = f'{self.base_url}{self.api_version}/project/{id}/check'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"

        # return data
        response = requests.get(self.api_validity_url, timeout=10)
        return response.status_code == 200
    
    def Project_Dependencies(self, id: str, data: list = None):
        """
        This function retrieves project dependencies data from an API endpoint and returns a list of results
        based on a provided data parameter.
        
        :param id: The id parameter is a string that represents the unique identifier of a project. It is
        used to retrieve the dependencies of a specific project
        :type id: str
        
        :param data: Optional parameter that takes a list of strings representing project slugs. If
        provided, the function will only return dependencies for the projects in the list. If not provided,
        the function will return dependencies for all projects in the specified project ID
        :type data: list
        
        :return: the result of a request to the API endpoint for project dependencies, filtered by the
        provided project ID. If a list of data is provided, the function will filter the results by the
        values in the list. The function returns a list of project dependencies, with each dependency
        represented as a dictionary containing information about the dependency project's ID, slug, and
        other details. If no ID or
        """

        
        # set API endpoint
        self.api_dependencies_url = f'{self.base_url}{self.api_version}/project/{id}/dependencies'
        
        # return error if no id or slug provided
        if id is None:
            return "Error: No id or slug provided"

        # make request
        project_data = self.__api_request(url=self.api_dependencies_url)
    
        
        return self.__list_result('slug', data, project_data['projects'])

    def multiple_Projects(self, ids: list, data: list = None):
        """
        This function takes a list of project IDs and returns project data for those IDs.
        
        :param ids: A list of project IDs to retrieve data for
        :type ids: list
        
        :param data: The `data` parameter is a list that contains additional data to be included in the
        response. It is an optional parameter and its default value is `None`
        :type data: list
        
        :return: the result of a request to the API endpoint for multiple projects, based on the provided
        list of project IDs. The returned data is processed and returned in a specific format using the
        private method `__list_result()`.
        """
        
        
        # set API endpoint
        self.api_multiple_projects_url = f'{self.base_url}{self.api_version}/projects'
        
        # return error if no id or slug provided
        if ids is None:
            return "Error: No id or slug provided"
        
        # params
        params = {
            'ids': json.dumps(ids)
        }
        
        # make request
        project_data = self.__api_request(url=self.api_multiple_projects_url, params=params)
 
        # return data
        return self.__list_result('slug', data, project_data)
    
    def random_Projects(self, count: int, data: list = None):
        """
        This function retrieves a specified number of random projects from an API endpoint and returns their
        slugs.
        
        :param count: The number of random projects to retrieve from the API
        :type count: int
        
        :param data: The `data` parameter is a list that contains the data to be searched for in the
        `project_data` returned by the API. The function will search for the `slug` attribute in the
        `project_data` and return only the items that match the `slug` values in the `data`
        :type data: list
        
        :return: the result of a request to the API endpoint for random projects, with a specified count of
        projects to be returned. If there is an error with the count parameter, an error message is
        returned. The function then returns a list of project slugs, either from the provided data list or
        from the API response.
        """
        
        # set API endpoint
        self.api_random_projects_url = f'{self.base_url}{self.api_version}/projects_random'
        
        # return error if no id or slug provided
        if count < 1:
            return "Error: Count must be greater than 0"
        
        # params
        params = {
            'count': count
        }
        
        # make request
        project_data = self.__api_request(url=self.api_random_projects_url, params=params)
        
        
        # return data
        return self.__list_result('slug', data, project_data)
        
    def project_Version(self, id: str, data: list = None):
        """
        This function retrieves project data based on the provided ID and returns the project name.
        
        :param id: The id parameter is a string that represents the unique identifier of a project version
        :type id: str
        
        :param data: The `data` parameter is a list that contains the specific fields of the project data
        that the user wants to retrieve. If `data` is not provided, the function will return all available
        data for the project
        :type data: list
        
        :return: the result of a request to an API endpoint for a specific project version identified by the
        provided id. The function returns the name of the project version if it exists, or an error message
        if no id or slug is provided. The function uses a helper method called "__api_request" to make the
        API request and another helper method called "__dict_result" to extract the name of the
        """
        
        # set API endpoint
        self.api_version_url = f'{self.base_url}{self.api_version}/version/{id}'
        
        # return error if no id or slug provided
        if id is None:
            return "Error: No id or slug provided"
        
        # make request
        project_data = self.__api_request(url=self.api_version_url)
        
        # return data
        return self.__dict_result('name', data, project_data)

    def list_Project_Versions(self, id: str, data: list = None, loaders: list = None, game_versions: list = None, featured: bool = False, ):
        """
        This function lists the versions of a project based on the provided parameters.
        
        :param id: The ID of the project for which to list versions
        :type id: str
        
        :param data: A list of data to be used for filtering or sorting the results of the API request. It
        is an optional parameter and defaults to None if not provided
        :type data: list
        
        :param loaders: A list of loader IDs to filter the project versions by. If None, all loaders will be
        included
        :type loaders: list
        
        :param game_versions: A list of game versions to filter the project versions by
        :type game_versions: list
        
        :param featured: A boolean parameter that determines whether to only return featured project
        versions or not. If set to True, only featured project versions will be returned. If set to False,
        all project versions will be returned, defaults to False
        :type featured: bool (optional)
        
        :return: the result of a list of project versions based on the provided parameters, including the
        project ID, data, loaders, game versions, and whether the versions are featured or not. The function
        is also returning an error message if no ID or slug is provided. The result is being returned using
        the private method `__list_result`.
        """

        # set API endpoint
        self.api_list_version_url = f'{self.base_url}{self.api_version}/project/{id}/version'      

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
        project_data = self.__api_request(url=self.api_list_version_url, params=params)

        # return data
        return self.__list_result('id', data, project_data)

    def multiple_Project_Versions(self, ids: list, data: list = None):
        """
        This function retrieves data for multiple project versions based on their IDs.
        
        :param ids: A list of project version IDs to retrieve data for
        :type ids: list
        
        :param data: The data parameter is a list that contains additional data to be included in the API
        request. It is an optional parameter and defaults to None if not provided
        :type data: list
        
        :return: the result of calling the private method `__list_result()` with the arguments `'name'`,
        `data`, and `project_data`. The content of this result depends on the implementation of the
        `__list_result()` method, which is not shown in the code snippet.
        """
        
        # set API endpoint
        self.api_multiple_versions_url = f'{self.base_url}{self.api_version}/versions'
        
        # return error if no id or slug provided
        if ids is None:
            return "Error: No id or slug provided"
        
        # params
        params = {
            'ids': json.dumps(ids)
        }
        
        # make request
        project_data = self.__api_request(url=self.api_multiple_versions_url, params=params)
 
        # return data
        return self.__list_result('name', data, project_data)

    def project_Versions_Hash(self, hash: str, data: list = None):
        """
        This function takes a hash and an optional list of data, sets an API endpoint, makes a request, and
        returns a dictionary result based on the name key.
        
        :param hash: The hash parameter is a string that represents the unique identifier of a version file
        in the API
        :type hash: str
        
        :param data: The `data` parameter is a list that can be used to filter the results returned by the
        API. It is an optional parameter, meaning that if it is not provided, all the data associated with
        the specified hash will be returned. If it is provided, only the data that matches the values in
        :type data: list
        
        :return: the result of calling the private method `__dict_result()` with the arguments `'name'`,
        `data`, and `project_data`. The value returned by `__dict_result()` is the final output of the
        function.
        """
        
        # set API endpoint
        self.api_project_versions_hash_url = f'{self.base_url}{self.api_version}/version_file/{hash}'
        
        # return error if no id or slug provided
        if hash is None:
            return "Error: No hash provided"
        
        # make request
        project_data = self.__api_request(url=self.api_project_versions_hash_url)

        # return data
        return self.__dict_result('name', data, project_data)

    def user(self, id: str = None, username: str = None, data: list = None):
        """
        This function retrieves user data from an API endpoint based on either an ID or a username.
        
        :param id: a string representing the unique identifier of a user in the API's database
        :type id: str
        
        :param username: a string representing the username of the user being queried
        :type username: str
        
        :param data: The `data` parameter is a list that contains the specific fields or attributes of the
        user object that the user wants to retrieve. If `data` is not provided, the function will return all
        available data for the user
        :type data: list
        
        :return: the result of a request to the API endpoint for a specific user, based on either their ID
        or username. If no ID or username is provided, an error message is returned. The function then
        returns the requested data in a dictionary format.
        """
            
            # set API endpoint
        self.api_user_url = f'{self.base_url}{self.api_version}/user/{id or username}'
            
        # return error if no id or slug provided
        if id is None and username is None:
                return "Error: No id or username provided"
            
        # make request
        project_data = self.__api_request(url=self.api_user_url)

            
        # return data
        return self.__dict_result('username', data, project_data)
        
    def authenticated_User(self, data: list = None):
        """
        This function retrieves the username of an authenticated user through an API request.
        
        :param data: The `data` parameter is a list that contains the keys of the specific data that the
        user wants to retrieve from the API response. If `data` is not provided, the function will return
        the entire API response
        :type data: list
        
        :return: The method `authenticated_User` is returning the result of the private method
        `__dict_result` with the parameters `'username'`, `data`, and `project_data`. The content of the
        `project_data` variable is the result of an API request to the endpoint
        `self.api_user_from_auth_url`.
        """  
       
               # return error if no token provided
        if self.token is None:
            return "Error: No token provided"
        
        # set API endpoint
        self.api_user_from_auth_url = f'{self.base_url}{self.api_version}/user'
            
        # make request
        project_data = self.__api_request(url=self.api_user_from_auth_url)
            
        # return data
        if project_data is not None:
            return self.__dict_result('username', data, project_data)

    def multiple_Users(self, ids: list = None, data: list = None):
        """
        This function takes a list of user IDs and returns their corresponding usernames from an API
        endpoint.
        
        :param ids: A list of user IDs for which data is requested
        :type ids: list
        
        :param data: The data parameter is a list that contains additional data that can be used to filter
        or manipulate the results returned by the API request
        :type data: list
        
        :return: the result of the API request made to retrieve data for multiple users based on the
        provided ids. The returned data is a list of dictionaries containing information about the users,
        with the 'username' field as the key. If no ids are provided, an error message is returned.
        """
                
            # set API endpoint
        self.api_multiple_users_url = f'{self.base_url}{self.api_version}/users'
                
        # return error if no ids provided
        if ids is None:
            return "Error: No ids provided"
                
        params = {
            'ids': json.dumps(ids)
        }
            
        # make request
        project_data = self.__api_request(url=self.api_multiple_users_url, params=params)
                
        # return data
        return self.__list_result('username', data, project_data)
        
    def user_Projects(self, id: str = None, username: str = None, data: list = None):
        """
        This function retrieves project data for a user based on their ID or username.
        
        :param id: The unique identifier of the user whose projects are being requested
        :type id: str
        
        :param username: A string representing the username of the user whose projects are being
        requested. This parameter is optional and can be set to None if the id parameter is provided
        :type username: str
        
        :param data: A list of project slugs to filter the results by. If provided, only projects with
        slugs in this list will be returned. If None, all projects will be returned
        :type data: list
        
        :return: the result of the API request made to retrieve project data for a user identified by
        their id or username. The data is returned in a list format with the project slugs as the keys and
        the project data as the values. If no id or username is provided, an error message is returned.
        """
                    
            # set API endpoint
        self.api_user_projects_url = f'{self.base_url}{self.api_version}/user/{id or username}/projects'
                    
        # return error if no id or slug provided
        if id is None and username is None:
            return "Error: No id or username provided"
                    
        # make request
        project_data = self.__api_request(url=self.api_user_projects_url)
                    
        # return data
        return self.__list_result('slug', data, project_data)

    def user_Notifications(self, id: str = None, username: str = None, data: list = None):
        """
        This function retrieves user notifications data from an API endpoint based on the provided user ID
        or username.
        
        :param id: The unique identifier of the user for whom notifications are being requested
        :type id: str
        
        :param username: The username of the user for whom the notifications are being requested
        :type username: str
        
        :param data: A list of data to filter the results by. The function will return only the
        notifications that match the data provided
        :type data: list
        
        :return: either an error message if no token or id/username is provided, or it makes an API request
        to retrieve user notifications data and returns the result by calling the private method
        `__list_result()`.
        """

        
        # return error if no token provided
        if self.token is None:
            return "Error: No token provided"
        
        # set API endpoint
        self.api_user_nofiications_url = f'{self.base_url}{self.api_version}/user/{id or username}/notifications'
            
        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"
        
        # make request
        project_data = self.__api_request(url=self.api_user_nofiications_url)
        
        # return data
        if project_data is not None:
            return self.__list_result('id', data, project_data)
        
    def user_Followed_Projects(self, username: str = None, id: str = None, data: list = None):
        
        # return error if no token provided
        if self.token is None:
            return "Error: No token provided"
        
        # set API endpoint
        self.api_user_followed_projects_url = f'{self.base_url}{self.api_version}/user/{id or username}/follows'
        
        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"
        
        # make request
        project_data = self.__api_request(url=self.api_user_followed_projects_url)
        
        # return data
        if project_data is not None:
            return self.__list_result('slug', data, project_data)
        
    def user_Payout_History(self, id: str = None, username: str = None, data: list = None):
        
        # return error if no token provided
        if self.token is None:
            return "Error: No token provided"
        
        # set API endpoint
        self.api_user_payout_history_url = f'{self.base_url}{self.api_version}/user/{id or username}/payouts'
        
        # return error if no id or username provided
        if id is None and username is None:
            return "Error: No id or username provided"
        
        # make request
        project_data = self.__api_request(url=self.api_user_payout_history_url)
        
        # return data
        if project_data is not None:
            return self.__dict_result('all_time', data, project_data)
        
    def project_Members(self, id: str = None, slug: str = None, data: list = None):
        
        # TODO: Get Working
        
        # set API endpoint
        self.api_project_members_url = f'{self.base_url}{self.api_version}/project/{id or slug}/members'
        
        # return error if no id or slug provided
        if id is None and slug is None:
            return "Error: No id or slug provided"
        
        # make request
        project_data = self.__api_request(url=self.api_project_members_url)
        
        # return data
        if project_data is not None:
            return self.__list_result(None, data, project_data)
        
# TODO: implement POST, PATCH, and DELETE requests

# Modrinth API DELETE class
class DELETE:
    def __init__(self):
        pass
    

# Modrinth API POST class
class POST:
    def __init__(self):
        pass
    
# Modrinth API PATCH class
class PATCH:
    def __init__(self):
        pass
