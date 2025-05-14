install:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

lint:
	flake8 gendiff

test:
	pytest

coverage:
	coverage run -m pytest && coverage report