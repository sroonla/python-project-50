from gendiff.generate_diff import generate_diff
import difflib


def test_generate_diff_flat_json():
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        format_name='stylish'
    )
    assert result == expected


def test_generate_diff_nested_json():
    with open('tests/fixtures/nested/expected_nested.txt') as f:
        expected = f.read()
    result = generate_diff(
        'tests/fixtures/nested/nested1.json',
        'tests/fixtures/nested/nested2.json',
        format_name='stylish'
    )
    if result != expected:
        diff = '\n'.join(difflib.ndiff(
            expected.splitlines(),
            result.splitlines()
        ))
        print("=== DIFFERENCE ===")
        print(diff)
        print("==================")
    assert result == expected
