from gendiff.gendiff import generate_diff


expected = open("tests/fixtures/expected.txt", "r")


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected.read()
