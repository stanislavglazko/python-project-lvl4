install:
	@poetry install

lint:
	@poetry run flake8 task_manager

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/

run:
	poetry run python manage.py runserver

.PHONY: install test lint selfcheck check build publish
