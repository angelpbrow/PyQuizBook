def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    newdict = dict(zip(keys,values))
    return newdict

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    #update() directly on dict1 returns None.
    #must first copy dict1 into a new dict3 before merging with dict2
    d3 = d1.copy()
    d3.update(d2)
    return d3

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    newdict = {lst:d1 for lst in lst}
    return newdict

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    newdict = {}
    for key in datadict:
        newdict[key] = keylist
    return newdict

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for keylist in datadict:
        del datadict[keylist]
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    #if the key exists in datadict return its value
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    #min() returns smallest item in an iterable
    temp = min(ddd.values())
    result = [key for key in ddd if ddd[key] == temp]
    return ' '.join(result)

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    #max() returns largest item in an iterable
    temp = max(ddd.values())
    result = [key for key in ddd if ddd[key] == temp]
    return ' '.join(result)
