"""Format diff according to formatter type."""

from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import json_format


def format_diff(diff, formatter_type):
    """
    Format diff according to formatter type.

    Args:
        diff (list): diff of two dictionaries
        formatter_type (str): format type for diff

    Returns:
        str
    """
    if formatter_type == 'plain':
        return plain(diff)
    elif formatter_type == 'json':
        return json_format(diff)
    return stylish(diff)
