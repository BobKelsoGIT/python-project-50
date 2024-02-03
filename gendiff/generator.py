def key_added(diff_lines, key, value):
    diff_lines.append({
        'name': key,
        'status': 'added',
        'new_value': value
    })


def key_deleted(diff_lines, key, value):
    diff_lines.append({
        'name': key,
        'status': 'deleted',
        'old_value': value
    })


def key_nested(diff_lines, key, value1, value2):
    nested_diff = generate_diff_list(value1, value2)
    diff_lines.append({
        'name': key,
        'status': 'nested',
        'nested_diff': nested_diff
    })


def key_changed(diff_lines, key, value1, value2):
    diff_lines.append({
        'name': key,
        'status': 'changed',
        'old_value': value1,
        'new_value': value2
    })


def key_unchanged(diff_lines, key, value):
    diff_lines.append({
        'name': key,
        'status': 'unchanged',
        'value': value
    })


def generate_diff_list(data1, data2) -> list:
    union_keys = data1.keys() | data2.keys()
    added_keys = data2.keys() - data1.keys()
    deleted_keys = data1.keys() - data2.keys()

    diff_lines = []

    for key in union_keys:
        value1, value2 = data1.get(key), data2.get(key)
        key_added(diff_lines, key, value2) if key in added_keys else None
        key_deleted(diff_lines, key, value1) if key in deleted_keys else None
        key_nested(diff_lines, key, value1, value2) if isinstance(value1, dict) and isinstance(value2,
                                                                                               dict) else None
        key_changed(diff_lines, key, value1, value2) if value1 != value2 else None
        key_unchanged(diff_lines, key, value1) if value1 == value2 else None

    return sorted(diff_lines, key=lambda x: x['name'])
