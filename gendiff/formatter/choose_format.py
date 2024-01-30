from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain


def formatted_output(diff, style='stylish'):
    if style == 'stylish':
        return make_stylish(diff)
    elif style == 'plain':
        return make_plain(diff)
    else:
        raise ValueError("Unsupported format")
