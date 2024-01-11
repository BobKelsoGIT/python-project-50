from gendiff.gendiff import generate_diff


expected_json = open("tests/fixtures/expected_json.txt", "r")
expected_yaml = open("tests/fixtures/expected_yml.txt", "r")


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected_json.read()


def test_generate_diff_yaml():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == expected_yaml.read()
