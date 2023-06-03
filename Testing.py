import os
import dotenv
from ModrinthAPIConnect.GET import Project, Version, User
from ModrinthAPIConnect.Config import set_Auth

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

search = proj.search(query="free", limit=1, offset=0, data=['project_id', 'title'], facets=[['versions:1.18.2'], ["project_type:mod"]], async_=True)
# print(search)


####################################################################################################

project = proj.get(slug='sodium', data=['title', 'id'], async_=True)
# print(project)

####################################################################################################


validate_Project = proj.validate(id='XeEZ3fK2')
# print(validate_Project)

####################################################################################################

Project_Dependencies = proj.dependencies(id='XeEZ3fK2', data=['title', 'id'])
# print(Project_Dependencies)

####################################################################################################

List_Project_Version = vers.get_List(id='XeEZ3fK2', game_versions=['1.19.2'], loaders=['fabric'], data=['version_number'], featured=False)
# print(List_Project_Version)

####################################################################################################

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