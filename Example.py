import os
import dotenv
from ModrinthAPIConnect.GET import Project, Version, User
from ModrinthAPIConnect.utils.Validate import set_Auth

# get your token from env file
dotenv.load_dotenv()
token = os.getenv('GITHUB_TOKEN')

# set your authentication
set_Auth(Token=f'{token}', GithubUsername='GentleWizard', Email='github@gentlewizard.ca')


proj = Project()
vers = Version()
user = User()

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

search = proj.search(query="free", limit=1, offset=0, data=['project_id', 'title'], facets=[['versions:1.18.2'], ["project_type:mod"]])
# print(search)


####################################################################################################

"""
The project function gets data from a specific project.

id: is a string of the project you want to get data from

data: is the data you want to get back, and is optional it defaults to showing all data
"""
project = proj.get(slug='sodium', data=['title', 'id'])
print(project)

####################################################################################################


"""
The validate_Project function checks if a project id is valid.

id: is a string of the project you want to check
"""
validate_Project = proj.validate(id='XeEZ3fK2')
# print(validate_Project)

####################################################################################################


"""
The Project_Dependencies function gets the dependencies of a project.

id: is a string of the project you want to get data from

data: is the data you want to get back, and is optional it defaults to showing all data
"""
Project_Dependencies = proj.dependencies(id='XeEZ3fK2', data=['title', 'id'])
# print(Project_Dependencies)

####################################################################################################


"""
The Project_Versions function gets the versions of a project.

id: is a string of the project you want to get data from

game_versions: is the game versions you want to get data for

loaders: are the mod loaders you want to get data for

featured: is if you want to get only featured versions or not

data: is the data you want to get back, and is optional it defaults to showing all data
"""
List_Project_Version = vers.get_List(id='XeEZ3fK2', game_versions=['1.19.2'], loaders=['fabric'], data=['version_number'], featured=False)
# print(List_Project_Version)

####################################################################################################

"""
The Multiple_Projects function gets data from multiple specified projects.

ids: is a list of srings of ids of the projects you want to get data from

data: is the data you want to get back, and is optional it defaults to showing all data. this is a list of strings
"""

multiple_projects = proj.get_Multiple(ids=['ttfYkIsI', 'XeEZ3fK2'], data=['title', 'id'])
# print(multiple_projects)

####################################################################################################

random_Project = proj.get_Random(count=2, data=['title', 'id'])
# print(random_Project)

####################################################################################################

Project_Version = vers.get(id='brPpY4rT', data=['id', 'version_number'])
# print(Project_Version)

####################################################################################################

Multiple_Project_versions = vers.get_Multiple(ids=['brPpY4rT', '5MFTTQBW'], data=['id', 'version_number'])
# print(Multiple_Project_versions)

####################################################################################################

Project_Versions_Hash = vers.get_From_Hash(hash='f1197c53e0743dc9af60f06b358dfed1f588b175', data=['id', 'game_versions'])
# print(Project_Versions_Hash)

####################################################################################################

User = user.get(id='7wY1ZtMM', data=['avatar_url', 'role', 'created'])
# print(User)

####################################################################################################

Your_Data = user.get_Authenticated(data=['id', 'github_id'])
# print(Your_Data)

####################################################################################################

Multiple_Users = user.get_Multiple(ids=['7wY1ZtMM', 'iFMgB5Ib'], data=['avatar_url', 'role', 'created'])
# print(Multiple_Users)

####################################################################################################

User_Projects = user.get_Projects(id='iFMgB5Ib', data=['title', 'id'])
# print(User_Projects)

####################################################################################################

User_notifcations = user.get_Notifications(id='7wY1ZtMM',data=['id', 'title', 'created'])
# print(User_notifcations)

####################################################################################################

User_Followed_Projects = user.get_Followed_Projects(id='7wY1ZtMM', data=['title', 'id'])
# print(User_Followed_Projects)

####################################################################################################

User_Payout_History = user.get_Payout_History(id='7wY1ZtMM', data=['last_month'])
# print(User_Payout_History)

####################################################################################################