import os
import json
import pytest
from gendiff import generate_diff

FIXTURES_PATH = "tests/fixtures"

test_cases = [
    ("nested/nested1.json", "nested/nested2.json"),
    ("recursive/json/recursive1.json", "recursive/json/recursive2.json"),
    ("recursive/yml/recursive1.yml", "recursive/yml/recursive2.yml"),
]


@pytest.mark.parametrize("file1, file2", test_cases)
def test_json_format(file1, file2):
    file_path1 = os.path.join(FIXTURES_PATH, file1)
    file_path2 = os.path.join(FIXTURES_PATH, file2)
    
    result = generate_diff(file_path1, file_path2, "json")
    
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    
    for node in parsed:
        assert 'key' in node
        assert 'type' in node
        assert node['type'] in [
            'nested', 'added', 'removed', 'unchanged', 'changed'
        ]
        
        if node['type'] == 'nested':
            assert 'children' in node
        elif node['type'] == 'changed':
            assert 'old_value' in node
            assert 'new_value' in node
        else:
            assert 'value' in node