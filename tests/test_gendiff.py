"""Test gendiff module."""

from gendiff.gendiff import generate_diff


def test_generate_diff_flat():
    """Test generate_diff function."""
    expected = open('tests/fixtures/expected_flat_diff.txt').read()

    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    assert generate_diff(file1_json, file2_json) == expected

    file1_yaml = 'tests/fixtures/file1.yml'
    file2_yaml = 'tests/fixtures/file2.yml'
    assert generate_diff(file1_yaml, file2_yaml) == expected
