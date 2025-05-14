from gendiff import generate_diff

def test_generate_diff_flat_json():
    expected = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    print(repr(result))
    assert result == expected
