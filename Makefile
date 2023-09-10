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