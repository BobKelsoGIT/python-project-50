import pytest

from gendiff.output import generate_diff


@pytest.fixture
def data1():
    return f"tests/fixtures/file1.yml"


@pytest.fixture
def data2():
    return f"tests/fixtures/file2.yml"


@pytest.fixture
def expected():
    with open('tests/fixtures/expected_yml.txt') as file:
        return file.read()


def test_gendiff(data1, data2, expected):
    # assert gendiff(data1, data2) == expected
    pass
