"""Generate diff from two files."""

import itertools

from gendiff.read_file import read_json


def get_value(dictionary, key):
    """
    Get value from object by key.

    Args:
        dictionary (dict): json.read result
        key: dict key

    Returns:
        obj value by key
    """
    if key not in dictionary:
        return None

    obj_val = dictionary[key]
    if isinstance(obj_val, bool):
        return str(obj_val).lower()
    return obj_val


def get_key_diff(indent_type, key, obj_val):
    """
    Get diff between values by one key.

    Args:
        indent_type: str
        key: objects key
        obj_val: object value by key

    Returns:
        str: diff of two values
    """
    indents = {
        'add': '  + ',
        'remove': '  - ',
        'same': '    ',
    }

    return f'{indents[indent_type]}{key}: {obj_val}'


def generate_diff(file1_path, file2_path):
    """
    Generate diff from two files.

    Args:
        file1_path (str): first file path
        file2_path (str): second file path

    Returns:
        str: two files diff
    """
    json_obj1 = read_json(file1_path)
    json_obj2 = read_json(file2_path)

    all_keys = set(json_obj1) | set(json_obj2)
    diff_list = []

    for key in sorted(all_keys):
        value1 = get_value(json_obj1, key)
        value2 = get_value(json_obj2, key)
        if key not in json_obj1:
            diff_list.append(get_key_diff('add', key, value2))
        elif key not in json_obj2:
            diff_list.append(get_key_diff('remove', key, value1))
        else:
            if value1 == value2:
                diff_list.append(get_key_diff('same', key, value1))
            else:
                diff_list.append(get_key_diff('remove', key, value1))
                diff_list.append(get_key_diff('add', key, value2))

    diff = itertools.chain('{', diff_list, '}')
    return '\n'.join(diff)
