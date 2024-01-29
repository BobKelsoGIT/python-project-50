from gendiff.formatter.stylish import make_stylish


def formatted_output(diff, style='stylish'):
    if style == 'stylish':
        return make_stylish(diff)
    else:
        raise ValueError("Unsupported format")
