from gendiff.formatter.stylish import stylish_output


def formatted_output(diff, style='stylish'):
    if style == 'stylish':
        return stylish_output(diff)
    else:
        raise ValueError("Unsupported format")
