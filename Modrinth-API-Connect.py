# app to make requests to the Modrinth v2

import requests


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
        # url
        self.api_search_url = f'{self.base_url}{self.API_version}/search'
        
        # get search parameters
        self.search_params['query'] = query
        self.search_params['limit'] = limit
        self.facets = []
        self.offset = offset

        # make request
        response = requests.get(self.api_search_url, params=self.search_params)
        self.dict = response.json()

            
        # return data    
        keys = []
        if data is None:
            return self.dict

        for datum in data:
            info = datum.split()
            keys.extend(self.dict['hits'][0][key] for key in info)
        return keys
        
    # Get Project Details
    def get_Project(self, id: str, data: list = None):
        # url
        self.api_project_url = f'{self.base_url}{self.API_version}/project/{id}'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"
        
        response = requests.get(self.api_project_url)
        self.dict = response.json()

            
        # return data    
        keys = []   
        if data is None:
            return self.dict

        
        for datum in data:
            info = datum.split()
            keys.extend(self.dict[key] for key in info)
        return keys 
            
            
    # Validate Project       
    def validate_Project(self, id: str):
        # url
        self.api_validity_url = f'{self.base_url}{self.API_version}/project/{id}/check'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"
        
        response = requests.get(self.api_validity_url)
        return response.status_code == 200

            

    # Get Project Dependencies
    def get_Project_Dependencies(self, id: str, data: list = None):
        # url
        self.api_dependencies_url = f'{self.base_url}{self.API_version}/project/{id}/dependencies'
        
        # make request
        if id is None:
            return "Error: No id or slug provided"

        response = requests.get(self.api_dependencies_url)
        self.dict = response.json()

        # return data
        keys = []
        if data is None:
            return self.dict

        for datum in data:
            info = datum.split()
            for project in self.dict['projects']:
                keys.extend(project[key] for key in info)
        return keys
            
        
            
    
    # Get Project Version
    def get_Project_Version(self, id: str, data: list = None, loaders: list = None, game_versions: list = 'None', featured: bool = False):
        # TODO: 
        # url
        self.api_version_url = f'{self.base_url}{self.API_version}/project/{id}/version'
        
        # get version parameters
        if featured:
            featured = 'true'
        else:
            featured = 'false'

        self.version_params = {
            'loaders': loaders,
            'game_versions': game_versions,
            'featured': featured,
        }
        # make request
        if id is None:
            return "Error: No id or slug provided"

        response = requests.get(self.api_version_url, params=self.version_params)
        self.dict = response.json()
                
        # return data
        keys = []                
        if data is None:
            return self.dict

        for datum in data:
            info = datum.split()
            for project in self.dict:
                keys.extend(project[key] for key in info)
        return keys
        

    
    
print(ModrinthAPI().search(query='free', limit=1, offset=0, data=['project_id']))
print(ModrinthAPI().get_Project(id='XeEZ3fK2', data=['id']))
print(ModrinthAPI().validate_Project(id='XeEZ3fK2'))
print(ModrinthAPI().get_Project_Dependencies(id='XeEZ3fK2', data=['title']))
print(ModrinthAPI().get_Project_Version(id='XeEZ3fK2', data=['id'], featured=False, game_versions=['1.16.5'], loaders=['fabric']))