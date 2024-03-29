import pytest
from gendiff.generator import generate_diff_list, nested


@pytest.fixture
def initial_data():
    return {
        'first_level': {
            'second_level1': False,
            'second_level2': 'foo'
        }
    }


@pytest.fixture
def modified_data():
    return {
        'first_level': {
            'second_level1': True,
            'second_level2': 'foo',
            'second_level3': 'baz'
        }
    }


@pytest.fixture
def test_result():
    return [
        {
            'name': 'first_level',
            'status': 'nested',
            'children': [
                {'name': 'second_level1', 'status': 'changed', 'old_value': False, 'new_value': True},
                {'name': 'second_level2', 'status': 'unchanged', 'value': 'foo'},
                {'name': 'second_level3', 'status': 'added', 'new_value': 'baz'},
            ]
        }
    ]


def test_generate_diff_list(initial_data, modified_data, test_result):
    result = generate_diff_list(initial_data, modified_data)
    assert result == test_result


def test_nested():
    old_value = {'key': 'error',
                 'number': 5}
    new_value = {'add': 'poncho',
                 'key': 'successfully',
                 'number': 5}
    result = nested('nested_key', old_value, new_value)

    assert result == {
        'name': 'nested_key',
        'status': 'nested',
        'children': [
            {'name': 'add', 'status': 'added', 'new_value': 'poncho'},
            {'name': 'key', 'status': 'changed', 'old_value': 'error', 'new_value': 'successfully'},
            {'name': 'number', 'status': 'unchanged', 'value': 5},
        ]
    }
