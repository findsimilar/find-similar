test:
	pytest

coverage:
	pytest -s --cov --cov-report html --cov-fail-under 95

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
	cd .. &\
	pylint -j 0 --ignore venv --recursive=y $(shell pwd)

full-lint:
	make yamllint
	make pylint

lint:
	@if [ "$(shell git ls-files -m '*.py')" != "" ]; then\
        pylint $(shell git ls-files -m '*.py');\
    fi
