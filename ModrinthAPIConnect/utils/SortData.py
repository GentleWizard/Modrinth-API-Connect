def dict_result(omit, data, project_data):
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
    
def list_result(omit, data, project_data):
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