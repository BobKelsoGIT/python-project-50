install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

install-package:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff