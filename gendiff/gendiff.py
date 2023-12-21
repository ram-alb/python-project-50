"""Generate diff from two files in different formats."""

from gendiff.compare import compare_dicts
from gendiff.formatter import format_diff
from gendiff.parser import parse_file


def generate_diff(file1_path, file2_path, formatter_type='stylish'):
    """
    Generate diff comparing two json, yaml files.

    Args:
        file1_path (str): path to first file
        file2_path (str): path to second file
        formatter_type (str): the format in which the diff will be formatted

    Returns:
        diff (str)
    """
    supported_formatter_types = {'stylish', 'plain', 'json'}

    if formatter_type not in supported_formatter_types:
        return (
            'formatter_type parameter can only take the following values: '
            f'plain, json, stylish. Current value is {formatter_type}'
        )

    try:
        dict1 = parse_file(file1_path)
        dict2 = parse_file(file2_path)
    except ValueError as err:
        return str(err)

    diff = compare_dicts(dict1, dict2)

    return format_diff(diff, formatter_type)
