from gendiff import generate_diff
import os


def get_fixture_path(filename):
    return os.path.join('tests', 'fixtures', filename)


def test_flat_yaml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = get_fixture_path('expected_flat.txt')
    
    with open(expected) as f:
        expected_output = f.read().rstrip()

    result = generate_diff(file1, file2, stringify=False)
    print(result)
    print(repr(expected_output))  # отладка
    assert result == expected_output
