import requests
from ModrinthAPIConnect.utils.Validate import return_Auth

Auth = return_Auth()

def Request(url, params: str = ""):
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
        response = requests.get(url, params=params, headers=Auth, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(err)