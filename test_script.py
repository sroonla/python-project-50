from gendiff import generate_diff

diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
print(diff)
