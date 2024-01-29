def nested(key, value1, value2):
    return {
        'name': key,
        'status': 'nested',
        'children': generate_diff_list(value1, value2)
    }


def generate_diff_list(data1, data2):
    keys_union = data1.keys() | data2.keys()
    added_keys = data2.keys() - data1.keys()
    deleted_keys = data1.keys() - data2.keys()

    diff_lines = []

    for key in keys_union:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in added_keys:
            diff_lines.append({
                'name': key,
                'status': 'added',
                'new_value': value2})
        elif key in deleted_keys:
            diff_lines.append({
                'name': key,
                'status': 'deleted',
                'old_value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff_lines.append(nested(key, value1, value2))
        elif value1 != value2:
            diff_lines.append({'name': key,
                               'status': 'changed',
                               'old_value': value1,
                               'new_value': value2})
        else:
            diff_lines.append({'name': key,
                               'status': 'unchanged',
                               'value': value1})

    sorted_diff = sorted(diff_lines, key=lambda x: x['name'])

    return sorted_diff
