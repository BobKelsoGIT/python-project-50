import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def initial_data():
    return "tests/fixtures/file1.yml"


@pytest.fixture
def modified_data():
    return "tests/fixtures/file2.yml"


@pytest.fixture
def expected_stylish():
    with open('tests/fixtures/expected_stylish.txt') as file:
        return file.read()


@pytest.fixture
def expected_json():
    with open('tests/fixtures/expected_json.txt') as file:
        return file.read()


@pytest.fixture
def expected_plain():
    with open('tests/fixtures/expected_plain.txt') as file:
        return file.read()


@pytest.mark.parametrize("expected_result, formatter", [
    (expected_stylish, "stylish"),
    (expected_json, "json"),
    (expected_plain, "plain"),
])
def test_generate_diff(initial_data, modified_data, expected_result, formatter):
    result = generate_diff(initial_data, modified_data, style=formatter)
    assert result == expected_result
