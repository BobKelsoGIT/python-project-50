import json


def make_json(diff) -> str:
    return json.dumps(diff, indent=4, separators=(',', ': '))
