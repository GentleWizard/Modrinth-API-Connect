from ModrinthAPIConnect import GET
# from ModrinthAPIConnect import POST
# from ModrinthAPIConnect import DELETE
# from ModrinthAPIConnect import PATCH

get = GET()
# post = POST() # Not yet implemented
# delete = DELETE() # Not yet implemented
# patch = PATCH() # Not yet implemented



####################################################################################################
#                                       GET requests                                               #
####################################################################################################

"""
The search function searches the modrinth api for mods.

query: is the search term

limit: is the amount of results you want

offset: is the amount of results you want to skip

facets: is the facets you want to filter by, and is optional. syntax: [[filter2:value1], [filter2:value2, ect...]]
each facet is a piece of data you can receive from the api, and the value is the value you want to filter by

data: is the data you want to get back, and is optional it defaults to showing all data

"""
search = get.search(query="free", limit=5, offset=0, data=['project_id', 'title', 'versions'], facets=[['versions:1.18.2'], ["project_type:mod"]])
print(search)

####################################################################################################

"""
The project function gets data from a specific project.

id: is the id of the project you want to get data from

data: is the data you want to get back, and is optional it defaults to showing all data
"""
project = get.project(id='XeEZ3fK2', data=['title', 'id'])

####################################################################################################


"""
The validate_Project function checks if a project id is valid.

id: is the id of the project you want to check
"""
validate_Project = get.validate_Project(id='XeEZ3fK2')

####################################################################################################


"""
The Project_Dependencies function gets the dependencies of a project.

id: is the id of the project you want to get data from

data: is the data you want to get back, and is optional it defaults to showing all data
"""
Project_Dependencies = get.Project_Dependencies(id='XeEZ3fK2', data=['title', 'id'])

####################################################################################################


"""
The Project_Versions function gets the versions of a project.

id: is the id of the project you want to get data from

game_versions: is the game versions you want to get data for

loaders: are the mod loaders you want to get data for

featured: is if you want to get only featured versions or not

data: is the data you want to get back, and is optional it defaults to showing all data
"""
Project_Version = get.Project_Version(id='XeEZ3fK2', game_versions=['1.16.5'], loaders=['fabric', 'forge', 'quilt'], data=['id', 'version_number'], featured=False)

####################################################################################################

