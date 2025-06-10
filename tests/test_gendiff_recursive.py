from gendiff.generate_diff import generate_diff
import difflib


def test_recursive_json():
    expected = open(
        'tests/fixtures/recursive/json/expected_recursive.txt'
    ).read()
    result = generate_diff(
        'tests/fixtures/recursive/json/recursive1.json',
        'tests/fixtures/recursive/json/recursive2.json',
        format_name='stylish'
    )

    # Добавленная отладочная печать
    print("\n===== Expected Output =====\n")
    print(expected)
    print("\n===== Actual Output =====\n")
    print(result)
    print("\n===== Line-by-Line Diff =====")

    exp_lines = expected.splitlines()
    res_lines = result.splitlines()

    diff = difflib.ndiff(exp_lines, res_lines)
    print('\n'.join(diff))

    assert result == expected
