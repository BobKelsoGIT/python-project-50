from gendiff.parser import get_data


def generate_diff(file1, file2):
    data1 = get_data(file1)
    data2 = get_data(file2)
    keys_union = set(data1.keys()) | set(data2.keys())
    sorted_keys = sorted(keys_union)

    diff_lines = []

    for key in sorted_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_lines.append(f'    {key}: {data1[key]}')
            else:
                diff_lines.append(f'  - {key}: {data1[key]}')
                diff_lines.append(f'  + {key}: {data2[key]}')
        elif key in data1:
            diff_lines.append(f'  - {key}: {data1[key]}')
        elif key in data2:
            diff_lines.append(f'  + {key}: {data2[key]}')

    return '{\n' + '\n'.join(diff_lines) + '\n}'
