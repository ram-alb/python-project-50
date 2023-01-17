"""Generate diff from two files."""

from gendiff.compare import compare_dicts
from gendiff.formatters.stylish import stylish
from gendiff.read_file import read_file


def generate_diff(file1_path, file2_path):
    """
    Generate diff comparing two json, yaml files.

    Args:
        file1_path (str): path to first file
        file2_path (str): path to second file

    Returns:
        diff (str)
    """
    dict1 = read_file(file1_path)
    dict2 = read_file(file2_path)
    diff = compare_dicts(dict1, dict2)
    return stylish(diff)
