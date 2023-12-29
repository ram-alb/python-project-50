"""Test gendiff module."""

from pathlib import Path

import pytest
from gendiff.gendiff import generate_diff

FIXT_PATH = Path('tests/fixtures')
input_path = FIXT_PATH / 'input'
output_path = FIXT_PATH / 'output'

input_data = {
    file_path.name: file_path
    for file_path in input_path.iterdir()
}

output_data = {
    file_path.name: file_path
    for file_path in output_path.iterdir()
}


def read_file(file_path):
    with open(file_path, 'r') as file_obj:
        return file_obj.read()


@pytest.mark.parametrize(
    'diff,file1,file2',
    [
        ('flat_diff.txt', 'flat1.json', 'flat2.json'),
        ('flat_diff.txt', 'flat1.yaml', 'flat2.yaml'),
        ('nested_diff.txt', 'nested1.json', 'nested2.json'),
        ('nested_diff.txt', 'nested1.yml', 'nested2.yml'),
    ],
)
def test_generate_diff_stylish(diff, file1, file2):
    """Test generate_diff function with stylish output."""
    assert generate_diff(
        input_data[file1],
        input_data[file2],
    ) == read_file(output_data[diff])


@pytest.mark.parametrize(
    'diff,file1,file2',
    [
        ('plain_diff.txt', 'nested1.json', 'nested2.json'),
        ('plain_diff.txt', 'nested1.yml', 'nested2.yml'),
    ],
)
def test_generate_diff_plain(diff, file1, file2):
    """Test generate_diff function with plain output."""
    assert generate_diff(
        input_data[file1],
        input_data[file2],
        'plain',
    ) == read_file(output_data[diff])


@pytest.mark.parametrize(
    'diff,file1,file2',
    [
        ('json_diff.txt', 'nested1.json', 'nested2.json'),
        ('json_diff.txt', 'nested1.yml', 'nested2.yml'),
    ],
)
def test_generate_diff_json(diff, file1, file2):
    """Test generate_diff function with json output."""
    assert generate_diff(
        input_data[file1],
        input_data[file2],
        'json',
    ) == read_file(output_data[diff])
