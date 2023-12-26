from pathlib import Path

from gendiff.gendiff import generate_diff

FIXT_PATH = Path('tests/fixtures/input')

flat1_json = FIXT_PATH / 'flat1.json'
flat2_json = FIXT_PATH / 'flat2.json'
file1_bat = FIXT_PATH / 'nested1.bat'
file2_bat = FIXT_PATH / 'nested2.bat'


def test_generate_diff_unssupported_formatter_type():
    """Test generate_diff function with unssupported formatter type."""
    formatter_type = 'some_type'
    expected = (
        'formatter_type parameter can only take the following values: '
        f'plain, json, stylish. Current value is {formatter_type}'
    )
    diff = generate_diff(flat1_json, flat2_json, formatter_type)

    assert diff == expected


def test_generate_diff_unssupported_file_type():
    """Test generate_diff function with unssupported file type."""
    expected = (
        'Unsupported file type: ".bat". '
        'Supported file types: .json, .yml, .yaml'
    )
    diff = generate_diff(file1_bat, file1_bat)
    assert diff == expected
