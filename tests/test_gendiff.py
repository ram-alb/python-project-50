"""Test gendiff module."""

from gendiff.gendiff import generate_diff


def test_generate_diff():
    """Test generate_diff function."""
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(file1_path, file2_path) == expected
