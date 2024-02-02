from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make_json


def format_output(diff, style='stylish'):
    """
    Select a formatter depending on the user's specified preference
    """
    if style == 'stylish':
        return make_stylish(diff)
    elif style == 'plain':
        return make_plain(diff)
    elif style == 'json':
        return make_json(diff)
    else:
        raise ValueError("Unsupported format")
