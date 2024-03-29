INDENT_SYMBOL = ' '
ADDED_SYMBOL = '+ '
REMOVED_SYMBOL = '- '
UNCHANGED_SYMBOL = '  '


def to_str(value, indent=2) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        spaces = INDENT_SYMBOL * (indent + 4)
        result = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, indent + 4)
            result.append(f"{spaces}{UNCHANGED_SYMBOL}{key}: {formatted_value}")
        formatted_string = '\n'.join(result)
        end_indent = INDENT_SYMBOL * (indent + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish(diff, indent=2) -> str:
    result = []
    spaces = INDENT_SYMBOL * int(indent)
    for item in diff:
        name = item.get('name')
        status = item.get('status')
        old_value = to_str(item.get("old_value"), indent)
        new_value = to_str(item.get("new_value"), indent)

        if status == 'unchanged':
            value = to_str(item.get("value"), indent)
            result.append(f"{spaces}{UNCHANGED_SYMBOL}{name}: {value}")
        elif status == 'added':
            result.append(f"{spaces}{ADDED_SYMBOL}{name}: {new_value}")
        elif status == 'deleted':
            result.append(f"{spaces}{REMOVED_SYMBOL}{name}: {old_value}")
        elif status == 'changed':
            result.append(f"{spaces}{REMOVED_SYMBOL}{name}: {old_value}\n"
                          f"{spaces}{ADDED_SYMBOL}{name}: {new_value}")
        elif status == 'nested':
            children = make_stylish(item.get("children"), indent + 4)
            result.append(f"{spaces}{UNCHANGED_SYMBOL}{name}: {children}")
    styled = '\n'.join(result)
    ending = INDENT_SYMBOL * (indent - 2)

    return f"{{\n{styled}\n{ending}}}"
