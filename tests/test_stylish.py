import json
from gendiff.formatter.stylish import make_stylish, to_str


def test_make_stylish():
    diff = json.load(open('tests/fixtures/diff.json'))

    expected_result = """{
  + key1: value1
  - key2: value2
  - key3: value3
  + key3: value3_updated
    key4: value4
    nested_key: {
      + nested_key2: value2_nested
    }
}"""

    result = make_stylish(diff)
    assert expected_result == result


def test_to_str():
    assert to_str(None) == 'null'
    assert to_str(True) == 'true'
    assert to_str(False) == 'false'
    assert to_str(42) == '42'
    assert to_str('hello') == 'hello'
    assert to_str({
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }) == '''{
        host: hexlet.io
        timeout: 50
        proxy: 123.234.53.22
        follow: false
    }'''
