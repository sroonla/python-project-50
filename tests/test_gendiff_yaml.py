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
    
    # Добавленная отладочная печать
    print("\n===== Expected Output =====\n")
    print(expected)
    print("\n===== Actual Output =====\n")
    print(result)
    print("\n===== Line-by-Line Diff =====")
    
    # Сравнение построчно
    exp_lines = expected.splitlines()
    res_lines = result.splitlines()
    
    diff = difflib.ndiff(exp_lines, res_lines)
    print('\n'.join(diff))
    assert result == expected