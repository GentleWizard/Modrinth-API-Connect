"""
---

## Author: GentleWizard
### Github: https://github.com/GentleWizard/Modrinth-API-Connect
In development

---
## Description: 

This Python package is a Group of module that allows you to connect to the Modrinth API and modify data/retieve data from it.

---

GET: This module is for retrieving data from the Modrinth API.

DELETE: This module is for deleting data from the Modrinth API

POST: This module is for posting data to the Modrinth API

PATCH: This module is for patching data to the Modrinth API

---

### License: MIT
"""

from ModrinthAPIConnect.GET import Project, Version, User
from ModrinthAPIConnect.Settings import set_Auth
