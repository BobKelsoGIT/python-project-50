import json
from gendiff.formatter.plain import to_str, make_plain, get_path_and_values

BEGINNING = 'Property '


def test_to_str():
    assert to_str(None) == 'null'
    assert to_str(True) == 'true'
    assert to_str(False) == 'false'
    assert to_str(42) == '42'
    assert to_str('hello') == 'hello'
    assert to_str({'key': 'value'}) == '[complex value]'


def test_get_path_and_values():
    item_added = {'name': 'key1', 'status': 'added', 'new_value': 'value1'}
    item_removed = {'name': 'key2', 'status': 'deleted', 'old_value': 'value2'}
    item_changed = {'name': 'key3', 'status': 'changed', 'old_value': 'value3', 'new_value': 'value3_updated'}
    item_nested = {'name': 'nested_key', 'status': 'nested', 'children': [
        {'name': 'nested_key2', 'status': 'added', 'new_value': 'value2_nested'}
    ]}

    result_added = get_path_and_values(item_added)
    assert result_added == f"{BEGINNING}'key1' was added with value: 'value1'"

    result_removed = get_path_and_values(item_removed)
    assert result_removed == f"{BEGINNING}'key2' was removed"

    result_changed = get_path_and_values(item_changed)
    assert result_changed == f"{BEGINNING}'key3' was updated. From 'value3' to 'value3_updated'"

    result_nested = get_path_and_values(item_nested)
    assert result_nested == f"{BEGINNING}'nested_key.nested_key2' was added with value: 'value2_nested'"


def test_make_plain():
    diff = json.load(open('tests/fixtures/diff.json'))

    expected_result = (
        "Property 'key1' was added with value: 'value1'\n"
        "Property 'key2' was removed\n"
        "Property 'key3' was updated. From 'value3' to 'value3_updated'\n"
        "Property 'nested_key.nested_key2' was added with value: 'value2_nested'"
    )

    result = make_plain(diff)
    assert result == expected_result
