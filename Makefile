install:
	python3 -m venv .venv
	.venv/bin/pip install uv
	.venv/bin/uv pip install -e .[dev]

lint:
	.venv/bin/flake8 gendiff

test:
	.venv/bin/python -m pytest --cov=gendiff --cov-report=term-missing

coverage:
	.venv/bin/coverage run -m pytest
	.venv/bin/coverage report

update-fixtures:
	. .venv/bin/activate && gendiff tests/fixtures/recursive/json/recursive1.json tests/fixtures/recursive/json/recursive2.json > tests/fixtures/recursive/json/expected_recursive.txt
	. .venv/bin/activate && gendiff tests/fixtures/recursive/yml/recursive1.yml tests/fixtures/recursive/yml/recursive2.yml > tests/fixtures/recursive/yml/expected_recursive_yaml.txt
	. .venv/bin/activate && gendiff tests/fixtures/file1.json tests/fixtures/file2.json > tests/fixtures/expected_flat.txt

clean:
	rm -rf .venv .pytest_cache .coverage
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -delete