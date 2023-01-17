"""Read files."""

import json
import os
import pathlib

from yaml import CLoader as Loader
from yaml import load as yaml_load


def read_json(file_path):
    """
    Read json file.

    Args:
        file_path (str): json file path

    Returns:
        dict
    """
    abs_path = os.path.abspath(file_path)
    with open(abs_path) as json_file:
        return json.load(json_file)


def read_yaml(file_path):
    """
    Read yaml file.

    Args:
        file_path (str): yaml file path

    Returns:
        dict
    """
    abs_path = os.path.abspath(file_path)
    with open(abs_path) as yaml_file:
        return yaml_load(yaml_file, Loader=Loader)


def read_file(file_path):
    """
    Read json or yaml file.

    Args:
        file_path (str): file path

    Returns:
        dict
    """
    file_extension = pathlib.Path(file_path).suffix
    if file_extension in {'.yml', '.yaml'}:
        return read_yaml(file_path)
    return read_json(file_path)
