SEPARATOR = '.'
BEGINNING = 'Property '


def to_str(value) -> str:
    result = None

    if value is None:
        result = 'null'
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, (list, dict)):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f"'{value}'"
    else:
        result = str(value)

    return result


def get_path_and_values(item, path='') -> str:
    name = item.get('name')
    status = item.get('status')
    current_path = f'{path}{SEPARATOR}{name}' if path else f'{name}'
    old_value = to_str(item.get('old_value'))
    new_value = to_str(item.get('new_value'))

    if status == 'added':
        return (f"{BEGINNING}'{current_path}' was added "
                f"with value: {new_value}")
    elif status == 'deleted':
        return f"{BEGINNING}'{current_path}' was removed"
    elif status == 'changed':
        return (f"{BEGINNING}'{current_path}' was updated. "
                f"From {old_value} to {new_value}")
    elif status == 'nested':
        child = item.get('children')
        return make_plain(child, current_path)


def make_plain(diff, path='') -> str:
    result = []
    for item in diff:
        formatted_item = get_path_and_values(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)
