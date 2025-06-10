import os
import pytest
from gendiff import generate_diff

FIXTURES_PATH = "tests/fixtures"

test_cases = [
    (
        "nested/nested1.json",
        "nested/nested2.json",
        "nested/expected_nested_plain.txt"
    ),
    (
        "recursive/json/recursive1.json",
        "recursive/json/recursive2.json",
        "recursive/expected_recursive_plain.txt"
    ),
    (
        "recursive/yml/recursive1.yml",
        "recursive/yml/recursive2.yml",
        "recursive/yml/expected_yaml_plain.txt"
    ),
]


@pytest.mark.parametrize("file1, file2, expected_file", test_cases)
def test_plain_format(file1, file2, expected_file):
    file_path1 = os.path.join(FIXTURES_PATH, file1)
    file_path2 = os.path.join(FIXTURES_PATH, file2)
    expected_path = os.path.join(FIXTURES_PATH, expected_file)

    assert os.path.exists(file_path1), f"File not found: {file_path1}"
    assert os.path.exists(file_path2), f"File not found: {file_path2}"
    assert os.path.exists(expected_path), f"File not found: {expected_path}"

    with open(expected_path, "r") as f:
        expected = f.read().strip()

    result = generate_diff(file_path1, file_path2, "plain").strip()
    print("\nActual result:")
    print(result)
    print("\nExpected result:")
    print(expected)
    assert result == expected
