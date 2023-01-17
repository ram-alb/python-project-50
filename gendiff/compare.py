"""Compare two dicts."""


def get_dict_value(dictionary, key):
    """
    Get value from dictionary by key.

    Args:
        dictionary (dict): json.read result
        key: dict key

    Returns:
        dict value by key
    """
    if key not in dictionary:
        return None

    dict_val = dictionary[key]
    if isinstance(dict_val, bool):
        return str(dict_val).lower()
    if dict_val is None:
        return 'null'
    return dict_val


def compare_dicts(dict1, dict2):
    """
    Compare two dicts.

    Args:
        dict1 (dict): first dictionary
        dict2 (dict): second dictionary

    Returns:
        (list): list of dicts
    """
    keys = set(dict1) | set(dict2)

    diff = []
    for key in sorted(keys):
        value1 = get_dict_value(dict1, key)
        value2 = get_dict_value(dict2, key)

        if key not in dict1:
            diff.append({'key': key, 'type': 'added', 'value': value2})
        elif key not in dict2:
            diff.append({'key': key, 'type': 'removed', 'value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            children = compare_dicts(value1, value2)
            diff.append({'key': key, 'type': 'complex', 'children': children})
        elif value1 != value2:
            diff.append({
                'key': key,
                'type': 'changed',
                'old-value': value1,
                'new-value': value2,
            })
        else:
            diff.append({'key': key, 'type': 'same', 'value': value1})

    return diff
