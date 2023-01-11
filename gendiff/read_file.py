"""Read files."""

import json
import os


def read_json(file_path):
    """
    Read json files.

    Args:
        file_path (str): json file path

    Returns:
        dict
    """
    abs_path = os.path.abspath(file_path)
    with open(abs_path) as json_file:
        return json.load(json_file)
