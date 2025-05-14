install:
	python3 -m venv venv && source venv/bin/activate && pip install .[dev]

lint:
	flake8 gendiff

test:
	pytest --cov=gendiff --cov-report=term-missing

coverage:
	coverage run -m pytest && coverage report --fail-under=80
