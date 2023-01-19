"""Format diff to plain format."""

from operator import itemgetter


def stringify(val):
    """
    Stringify value of diff.

    Args:
        val: diff value

    Returns:
        str
    """
    if isinstance(val, dict):
        return '[complex value]'
    if val in {'true', 'false', 'null'}:
        return val
    if isinstance(val, str):
        return f"'{val}'"
    return val


def get_plain_item(diff_item, ancestry):
    """
    Get diff item in plain format.

    Args:
        diff_item (dict): result of diff by one key
        ancestry: chain of ancestry keys in case of nested diff item

    Returns:
        str
    """
    if 'value' in diff_item:
        new_value = stringify(diff_item['value'])

    key, key_type = itemgetter('key', 'type')(diff_item)
    new_ancestry = f'{ancestry}.{key}' if ancestry else key
    if key_type == 'added':
        return (
            f"Property '{new_ancestry}' "
            f"was added with value: {new_value}"
        )
    elif key_type == 'removed':
        return f"Property '{new_ancestry}' was removed"
    elif key_type == 'changed':
        return (
            f"Property '{new_ancestry}' was updated. "
            f"From {stringify(diff_item['old-value'])} "
            f"to {stringify(diff_item['new-value'])}"
        )


def plain(diff):
    """
    Format diff to plain format.

    Args:
        diff (list): diff of two dictionaries

    Returns:
        str
    """
    def iter(data, ancestry=None):
        """
        Format diff to plain format in iter process.

        Args:
            data (list): item of diff
            ancestry: chain of keys in nested diff

        Returns:
            str
        """

        changed_data = filter(lambda item: item['type'] != 'same', data)
        result = []
        for element in changed_data:
            key, key_type = itemgetter('key', 'type')(element)
            new_ancestry = f'{ancestry}.{key}' if ancestry else key
            if key_type in {'added', 'removed', 'changed'}:
                result.append(get_plain_item(element, ancestry))
            elif key_type == 'complex':
                result.append(iter(element['children'], new_ancestry))
        return '\n'.join(result)

    return iter(diff)
