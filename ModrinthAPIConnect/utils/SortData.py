"""
This module contains functions for sorting and manipulating data.
"""

def dict_result(omit, data, project_data):

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
    
def list_result(omit = None, data = None, project_data = None):
    if omit is None:
        result = {}
        for dict in project_data:
            data_dict = {}
            if data is not None:
                for item in data:
                    key = item
                    value = dict.get(item, None)
                    data_dict[key] = value
            if omit is None:
                result[dict] = data_dict
        return result

    if omit is not None:           
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
        return result
    

