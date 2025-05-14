install:
	python3 -m venv venv && source venv/bin/activate && pip install .[dev]

lint:
	python -m flake8 gendiff

test:
	python -m pytest --cov=gendiff --cov-report=term-missing

coverage:
	python -m coverage run -m pytest && python -m coverage report
