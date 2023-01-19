"""Test gendiff module."""

from gendiff.gendiff import generate_diff

file1_json = 'tests/fixtures/nested1.json'
file2_json = 'tests/fixtures/nested2.json'
file1_yaml = 'tests/fixtures/nested1.yml'
file2_yaml = 'tests/fixtures/nested2.yml'


def test_generate_diff_flat():
    """Test generate_diff function with flat data."""
    expected = open('tests/fixtures/expected_flat_diff.txt').read()

    flat1_json = 'tests/fixtures/file1.json'
    flat2_json = 'tests/fixtures/file2.json'
    assert generate_diff(flat1_json, flat2_json) == expected

    flat1_yaml = 'tests/fixtures/file1.yml'
    flat2_yaml = 'tests/fixtures/file2.yml'
    assert generate_diff(flat1_yaml, flat2_yaml) == expected


def test_generate_diff_nested():
    """Test generate_diff function with nested data."""
    expected = open('tests/fixtures/expected_nested_diff.txt').read()

    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected


def test_generate_diff_plain():
    """Test generate_diff function with plain output."""
    expected = open('tests/fixtures/expected_plain_diff.txt').read()
    
    assert generate_diff(file1_json, file2_json, 'plain') == expected
    assert generate_diff(file1_yaml, file2_yaml, 'plain') == expected


def test_generate_diff_json():
    """Test generate_diff function with json output."""
    expected = open('tests/fixtures/json_diff.txt').read()
    
    assert generate_diff(file1_json, file2_json, 'json') == expected
    assert generate_diff(file1_yaml, file2_yaml, 'json') == expected
