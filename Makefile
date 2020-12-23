install:
	@poetry install

lint:
	@poetry run flake8

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

run:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test

requirements:
	poetry export -f requirements.txt -o requirements.txt

.PHONY: install test lint selfcheck check build publish
