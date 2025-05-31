install:
	python3 -m venv venv && source venv/bin/activate && pip install .[dev]

lint:
	python -m flake8 gendiff

test:
	python -m pytest --cov=gendiff --cov-report=term-missing

coverage:
	python -m coverage run -m pytest && python -m coverage report

update-fixtures:
	gendiff tests/fixtures/recursive/json/recursive1.json tests/fixtures/recursive/json/recursive2.json > tests/fixtures/recursive/json/expected_recursive.txt
	gendiff tests/fixtures/recursive/yml/recursive1.yml tests/fixtures/recursive/yml/recursive2.yml > tests/fixtures/recursive/yml/expected_recursive_yaml.txt
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json > tests/fixtures/expected_flat.txt
