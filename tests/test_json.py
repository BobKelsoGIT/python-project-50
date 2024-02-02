import json
from gendiff.formatter.json import make_json


def test_make_json():
    diff = json.load(open('tests/fixtures/diff.json'))

    expected_result = [
        {'name': 'key1', 'new_value': 'value1', 'status': 'added'},
        {'name': 'key2', 'old_value': 'value2', 'status': 'deleted'},
        {'name': 'key3', 'new_value': 'value3_updated', 'old_value': 'value3', 'status': 'changed'},
        {'name': 'key4', 'status': 'unchanged', 'value': 'value4'},
        {'children': [{'name': 'nested_key2', 'new_value': 'value2_nested', 'status': 'added'}], 'name': 'nested_key',
         'status': 'nested'}
    ]

    result = make_json(diff)
    result_as_json = json.loads(result)
    assert expected_result == result_as_json
