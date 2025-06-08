import difflib
from gendiff.generate_diff import generate_diff


def test_recursive_yaml():
    expected = open(
        'tests/fixtures/recursive/yml/expected_recursive_yaml.txt'
    ).read()
    result = generate_diff(
        'tests/fixtures/recursive/yml/recursive1.yml',
        'tests/fixtures/recursive/yml/recursive2.yml',
        format_name='stylish'
    )
    if result != expected:
        print('\n'.join(difflib.ndiff(
            expected.splitlines(),
            result.splitlines()
        )))
    assert result == expected
