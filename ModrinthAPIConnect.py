# Github: ** https://github.com/GentleWizard/Modrinth-API-Connect **

# The ModrinthAPIConnect module is a Python module that allows for searching and retrieving data from the Modrinth v2 API.
# The ModrinthAPI class is used to interact with the API and retrieve data from it.

import requests
import json


# This is a Python class for interacting with the Modrinth API, allowing for searching with various parameters.
class ModrinthAPI():
    def __init__(self, query: str='', limit: int=1, offset: int=0, facets: dict = None):
        self. facets = facets
        self.query = query
        self.limit = limit
        self.offset = offset
        
        if facets is None:
            facets = {"versions": [], "categories": [], "project_type": []}
        if self.limit < 1:
            self.limit = 1
        if self.offset < 0:
            self.offset = 0

        # TODO: add API key
        self.api_key = ""

        # API search URL
        self.base_url = 'https://api.modrinth.com/'
        self.API_version = 'v2'

        # search parameters
        self.search_params = {
            'query': self.query,
            'limit': self.limit,
            'offset': self.offset,
            'facets': self.facets,
        }
        
    # Search for projects
    def search(self, query: str, limit: int=1, offset: int=0, data: list = None):
        """
        The function takes a query, limit, offset, and data as parameters, makes a request to an API search
        endpoint, and returns specific data from the response based on the input data parameter.
        
        :param query: The search query string
        :type query: str
        
        :param limit: The maximum number of search results to return. Default value is 1, defaults to 1
        :type limit: int (optional)
        
        :param offset: The offset parameter is used to specify the starting point of the search results. It
        determines the number of search results that are skipped before returning the results. For example,
        if offset is set to 10, the search results will start from the 11th result, defaults to 0
        :type offset: int (optional)
        
        :param data: The `data` parameter is a list of strings that specify which fields of the search
        results to return. Each string in the list represents a field name, and the fields are returned as a
        list of values. If `data` is `None`, the entire search result dictionary is returned
        :type data: list 
        
        :return: either the entire JSON response from the search API or a list of values corresponding to
        the specified keys in the 'data' parameter.
        """
        # url
        self.api_search_url = f'{self.base_url}{self.API_version}/search'
        
        # get search parameters
        self.search_params['query'] = query
        self.search_params['limit'] = limit
        self.facets = []
        self.offset = offset

        # make request
        response = requests.get(self.api_search_url, params=self.search_params)
        project_data = response.json()

            
        # return data    
        keys = []
        if data is None:
            return project_data

        for datum in data:
            info = datum.split()
            keys.extend(project_data['hits'][0][key] for key in info)
        return keys
        

    def get_Project(self, id: str, data: list = None):
        """
        This function retrieves project data from an API based on an ID and returns specific data if
        requested.
        
        :param id: a string representing the ID of a project to retrieve from an API endpoint
        :type id: str
        
        :param data: data is a list of strings that specifies which information to retrieve from the
        project. Each string in the list represents a key in the project dictionary. The function will
        return the values of all the keys specified in the list for the given project ID. If data is None,
        the function will return the entire
        :type data: list
        
        :return: The function `get_Project` returns either the entire dictionary of project information if
        no specific data is requested, or a list of specific data requested by the `data` parameter. If
        there is an error and no `id` or `slug` is provided, an error message is returned.
        """
        # url
        self.api_project_url = f'{self.base_url}{self.API_version}/project/{id}'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"
        
        response = requests.get(self.api_project_url)
        project_data = response.json()

            
        # return data    
        keys = []   
        if data is None:
            return project_data

        for datum in data:
            info = datum.split()
            keys.extend(project_data[key] for key in info)
        return keys 
            
            

    def validate_Project(self, id: str):
        """
        This function validates a project ID by sending a GET request to a specific API endpoint and
        checking if the response status code is 200.
        
        :param id: The id parameter is a string that represents the unique identifier of a project. It is
        used to validate the existence of a project by making a GET request to the API endpoint
        :type id: str
        
        :return: a boolean value indicating whether the response status code is equal to 200 or not.
        """
        # url
        self.api_validity_url = f'{self.base_url}{self.API_version}/project/{id}/check'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"
        
        # return data
        response = requests.get(self.api_validity_url)
        return response.status_code == 200

            


    def get_Project_Dependencies(self, id: str, data: list = None):
        """
        This is a Python function that retrieves project dependencies based on an ID and returns either the
        full dictionary or a list of specified data.
        
        :param id: The id of the project for which dependencies are being requested
        :type id: str
        
        :param data: The `data` parameter is a list of strings that contains information about the project
        dependencies that the user wants to retrieve. Each string in the list specifies a key or attribute
        of the project dependencies that the user wants to retrieve. The function will return the values of
        these keys or attributes for each project dependency
        :type data: list 
        
        :return: either the dictionary of project dependencies if no data is provided, or a list of project
        dependencies keys based on the provided data.
        """
        # url
        self.api_dependencies_url = f'{self.base_url}{self.API_version}/project/{id}/dependencies'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"

        response = requests.get(self.api_dependencies_url)
        project_data = response.json()

        # return data
        keys = []
        if data is None:
            return project_data
        for datum in data:
            info = datum.split()
            for project in project_data['projects']:
                keys.extend(project[key] for key in info)
        return keys
            
        
            
    

    def get_Project_Version(self, id: str, data: list = None, loaders: list = None, game_versions: list = None, featured: bool = False):
        """
        This is a Python function that retrieves project version information based on provided parameters
        and returns the requested data.
        
        :param id: The ID of the project for which the version information is being requested
        :type id: str
        
        :param data: The `data` parameter is a list of strings that specify which information to extract
        from the API response. Each string in the list represents a key or nested key in the JSON response
        that the function will extract and return. If `data` is `None`, the function will return the entire
        JSON response
        :type data: list 
        
        :param loaders: A list of mod loaders to filter the project versions by. If not provided, all mod loaders
        will be returned
        :type loaders: list (optional)
        
        :param game_versions: This parameter is used to filter the project versions by game version. It
        takes a list of game versions as input. If not provided, all game versions will be returned
        :type game_versions: list (optional)
        
        :param featured: A boolean value indicating whether to only return featured versions of the project,
        defaults to False
        :type featured: bool (optional)
        
        :return: either the dictionary of project versions or a list of specific data keys from the project
        versions, depending on the input parameters.
        """
        # url
        self.api_version_url = f'{self.base_url}{self.API_version}/project/{id}/version'
        

        self.version_params = {
            'loaders': json.dumps(loaders),
            'game_versions': json.dumps(game_versions),
            'featured': 'true' if featured else 'false',
        }
        # make request
        if id is None:
            return "Error: No id or slug provided"

        response = requests.get(self.api_version_url, params=self.version_params)
        project_data = response.json()
        
       
        # return data
        keys = []                
        if data is None:
            return project_data

        for datum in data:
            info = datum.split()
            for project in project_data:
                keys.extend(project[key] for key in info)
        return keys
        
