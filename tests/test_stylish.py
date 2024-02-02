from gendiff.formatter.stylish import make_stylish, to_str


def test_make_stylish():
    value = [
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

    expected_result = """{
    first_level: {
      - second_level1: false
      + second_level1: true
        second_level2: foo
      + second_level3: baz
    }
}"""

    assert expected_result == make_stylish(value)


def test_to_str_true():
    value = True
    assert to_str(value) == 'true'


def test_to_str_false():
    value = False
    assert to_str(value) == 'false'


def test_to_str_none():
    value = None
    assert to_str(value) == 'null'


def test_to_str_dict():
    value = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    expected_result = '''{
        host: hexlet.io
        timeout: 50
        proxy: 123.234.53.22
        follow: false
    }'''

    assert to_str(value) == expected_result
