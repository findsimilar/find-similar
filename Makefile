test:
	pytest

coverage:
	pytest -s --cov --cov-report html --cov-fail-under 97

docs:
	pdoc ./find_similar/ -o ./.docs

yamllint:
	yamllint -d relaxed .

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall find-similar
	rm -rf dist
	rm -rf find_similar.egg-info

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint