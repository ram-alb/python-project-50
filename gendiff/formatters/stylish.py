"""Format diff to stylish format."""

import itertools
from operator import itemgetter

depth_space_count = 4
replacer = ' '


def stringify(data, depth):
    """
    Stringify data from different types.

    Args:
        data: some data type
        depth (int): indent depth

    Returns:
        string
    """

    def iter_(current_data, iter_depth):
        """
        Stringify data in iter process.

        Args:
            current_data: data item
            iter_depth (int): indent depth level

        Returns:
            string
        """
        if not isinstance(current_data, dict):
            return str(current_data)

        deep_indent_size = iter_depth + depth_space_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * iter_depth
        lines = []
        for key, val in current_data.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result_data = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result_data)

    return iter_(data, depth)


def stylish_item(key, key_type, value, depth, is_stringified=False):
    """
    Format diff item in stylish mode.

    Args:
        key: dicts key
        key_type (str): key type after dicts comparing
        value: dicts value by key
        depth (int): indent depth
        is_stringified (bool): is dict value stringified or not

    Returns:
        string
    """
    indents = {
        'added': '  + ',
        'removed': '  - ',
        'same': '    ',
    }
    legacy_indent = replacer * depth * depth_space_count
    new_depth = (depth + 1) * depth_space_count

    indent = indents[key_type]
    if is_stringified:
        stringified_val = value
    else:
        stringified_val = stringify(
            value,
            new_depth,
        )
    return f'{legacy_indent}{indent}{key}: {stringified_val}'


def stylish(diff):
    """
    Format diff in stylish format.

    Args:
        diff (list): list of dicts - result of dict comparing

    Returns:
        string
    """
    def iter_(data, depth):
        """
        Format diff in stylish format in iter process.

        Args:
            data (list): list of dicts - result of dict comparing
            depth (int): indent level

        Returns:
            string
        """
        lines = []
        for item in data:
            key, key_type = itemgetter('key', 'type')(item)
            if key_type in {'added', 'removed', 'same'}:
                lines.append(
                    stylish_item(key, key_type, item['value'], depth)
                )
            elif key_type == 'changed':
                old_value = stylish_item(
                    key,
                    'removed',
                    item['old-value'],
                    depth
                )
                new_value = stylish_item(key, 'added', item['new-value'], depth)
                lines.append(f'{old_value}\n{new_value}')
            elif key_type == 'complex':
                stringified_val = iter_(item["children"], depth + 1)
                lines.append(
                    stylish_item(key, 'same', stringified_val, depth, True)
                )

        spaces_befor_bracket = replacer * depth * depth_space_count
        result = itertools.chain('{', lines, [spaces_befor_bracket + '}'])

        return '\n'.join(result)

    return iter_(diff, 0)
