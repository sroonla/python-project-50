.PHONY: lint test

lint:
	ruff check gendiff tests

test:
	pytest -vv --color=yes --exitfirst tests