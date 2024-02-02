from gendiff.parser import get_data, get_extension


def test_get_extension():
    assert get_extension('file.json') == 'json'
    assert get_extension('file.yml') == 'yml'
    assert get_extension('file.yaml') == 'yaml'


def test_get_data_json():
    file_path = 'tests/fixtures/file1.json'
    result = get_data(file_path)
    expected_result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert result == expected_result
