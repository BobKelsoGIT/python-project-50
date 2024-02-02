import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("initial_data, modified_data, expected_result_path, formatter", [
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "tests/fixtures/expected_stylish.txt", "stylish"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "tests/fixtures/expected_json.txt", "json"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "tests/fixtures/expected_plain.txt", "plain"),
])
def test_generate_diff(initial_data, modified_data, expected_result_path, formatter):
    with open(expected_result_path) as file:
        expected_result = file.read()

    result = generate_diff(initial_data, modified_data, style=formatter)
    assert result == expected_result
