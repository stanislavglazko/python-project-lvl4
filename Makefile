install:
	@poetry install

lint:
	@poetry run flake8 task_manager

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

run:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt -o requirements.txt

.PHONY: install test lint selfcheck check build publish
