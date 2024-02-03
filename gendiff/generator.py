def generate_diff_list(data1, data2) -> list:
    diff_lines = []

    for key in set(data1.keys()) | set(data2.keys()):
        value1, value2 = data1.get(key), data2.get(key)

        if key in data2 and key not in data1:
            diff_lines.append({'name': key, 'status': 'added', 'new_value': value2})
        elif key in data1 and key not in data2:
            diff_lines.append({'name': key, 'status': 'deleted', 'old_value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff_lines.append({'name': key, 'status': 'nested', 'nested_diff': generate_diff_list(value1, value2)})
        elif value1 != value2:
            diff_lines.append({'name': key, 'status': 'changed', 'old_value': value1, 'new_value': value2})
        else:
            diff_lines.append({'name': key, 'status': 'unchanged', 'value': value1})

    return sorted(diff_lines, key=lambda x: x['name'])
