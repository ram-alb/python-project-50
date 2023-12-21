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
    formatters = {
        'plain': plain,
        'json': json_format,
        'stylish': stylish,
    }
    return formatters[formatter_type](diff)
