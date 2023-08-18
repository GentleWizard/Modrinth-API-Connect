from .utils.API_Request import request

import json

api_version = "v2"
base_url = f"https://api.modrinth.com/{api_version}"


def get(version_id: str):
    """
    The function retrieves a version of a project by its ID and returns a dictionary of the version's data.

    ---

    ### ---Parameters---

    :param version_id: The ID of the version to retrieve
    :type version_id: str

    :return: the result of a version query based on the provided parameters. The function returns a
    dictionary of version data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_version_url = f"{base_url}/version/{version_id}"

    # return error if no user_id or slug provided
    if version_id is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = request(api_version_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_list(
    project_id: str,
    loaders: list | None = None,
    game_versions: list | None = None,
    featured: bool = False,
):
    """
    The function retrieves a list of versions for a project with the given ID and returns a list of
    dictionaries containing the versions' data.

    ---

    ### ---Parameters---

    :param project_id: The ID of the project to retrieve versions for
    :type project_id: str

    :param loaders: A list of loaders to filter the versions by
    :type loaders: list (optional)

    :param game_versions: A list of game versions to filter the versions by
    :type game_versions: list (optional)

    :param featured: A boolean parameter that determines whether to only return featured versions or not.
    If set to True, only featured versions will be returned. If set to False, all versions will be returned.
    Defaults to False
    :type featured: bool (optional)

    :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
    contains keys representing the version's data and their corresponding values.
    """

    # set API endpoint
    api_list_version_url = f"{base_url}/project/{project_id}/version"

    # params
    params = {
        "loaders": json.dumps(loaders),
        "game_versions": json.dumps(game_versions),
        "featured": "true" if featured else "false",
    }

    # return error if no user_id or slug provided
    if project_id is None:
        return "Error: No user_id or slug provided"

    # make request
    response, status_code = request(api_list_version_url, params=params, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_multiple(version_ids: list):
    """
    The function retrieves multiple versions of a project by their IDs and returns a list of dictionaries
    containing the versions' data.

    ---

    ### ---Parameters---

    :param version_ids: A list of version IDs to retrieve
    :type version_ids: list

    :return: A list of dictionaries containing the versions' data. Each dictionary represents a version and
    contains keys representing the version's data and their corresponding values.
    """

    # set API endpoint
    api_multiple_versions_url = f"{base_url}/versions"

    # return error if no user_id or slug provided
    if version_ids is None:
        return "Error: No user_id or slug provided"

    # params
    params = {"user_ids": json.dumps(version_ids)}

    # make request
    response, status_code = request(
        api_multiple_versions_url, params=params, method="GET"
    )

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def get_from_hash(version_hash: str):
    """
    The function retrieves a version of a project by its hash and returns a dictionary of the version's data.

    ---

    ### ---Parameters---

    :param version_hash: The hash of the version to retrieve
    :type version_hash: str

    :return: the result of a version query based on the provided parameters. The function returns a
    dictionary of version data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_project_versions_hash_url = f"{base_url}/version_file/{version_hash}"

    # return error if no user_id or slug provided
    if version_hash is None:
        return "Error: No version_hash provided"

    # make request
    response, status_code = request(api_project_versions_hash_url, method="GET")

    if status_code != 200:
        print(f"Error: {response}")

    else:
        # return data
        return response


def edit_version(
    version_id: str,
    name: str,
    version_number: str,
    changelog: str,
    dependencies: list,
    game_versions: list,
    version_type: str,
    loaders: list,
    files: list,
    status: str,
    requested_status: str,
    primary_file: list[str, ...],
    file_types: list[object, ...],
    featured: bool = False,
):
    """
    The function edits a version of a project by its ID and returns a dictionary of the version's data.

    ---

    ### ---Parameters---

    :param version_id: The ID of the version to edit
    :type version_id: str

    :param name: The name of the version
    :type name: str

    :param version_number: The version number of the version
    :type version_number: str

    :param changelog: The changelog of the version
    :type changelog: str

    :param dependencies: The dependencies of the version
    :type dependencies: list

    :param game_versions: The game versions of the version
    :type game_versions: list

    :param version_type: The type of the version
    :type version_type: str

    :param loaders: The loaders of the version
    :type loaders: list

    :param files: The files of the version
    :type files: list

    :param status: The status of the version
    :type status: str

    :param requested_status: The requested status of the version
    :type requested_status: str

    :param primary_file: The primary file of the version
    :type primary_file: list

    :param file_types: The file types of the version
    :type file_types: list

    :param featured: A boolean parameter that determines whether to only return featured versions or not.
    If set to True, only featured versions will be returned. If set to False, all versions will be returned.
    Defaults to False
    :type featured: bool (optional)

    :return: the result of a version query based on the provided parameters. The function returns a
    dictionary of version data, with each key representing a piece of data and its corresponding value.
    """

    # set API endpoint
    api_version_url = f"{base_url}/version/{version_id}"

    # return error if no user_id or slug provided
    if version_id is None:
        return "Error: No user_id or slug provided"

    # params
    data = {
        "changelog": changelog,
        "game_versions": json.dumps(game_versions),
        "loaders": json.dumps(loaders),
        "featured": featured,
        "dependencies": json.dumps(dependencies),
        "version_type": version_type,
        "files": json.dumps(files),
        "status": status,
        "requested_status": requested_status,
        "primary_file": json.dumps(primary_file),
        "file_types": json.dumps(file_types),
        "name": name,
        "version_number": version_number,
    }

    # make request
    response, status_code = request(api_version_url, data=data, method="PATCH")

    if status_code != 204:
        print(f"Error: {response}")

    else:
        # return data
        return response
