test:
	python manage.py test

test-proximity:
	python manage.py test analysis.tests.tests_proximity

server:
	python manage.py runserver

coverage:
	coverage run --source='.' manage.py test
	coverage html --omit=laboratory/asgi.py,laboratory/wsgi.py,manage.py,analysis/management/*
	coverage report --omit=laboratory/asgi.py,laboratory/wsgi.py,manage.py,analysis/management/* --fail-under=100


migrate:
	python manage.py migrate

compare_two:
	python manage.py compare_two "$(one)" "$(two)"

example_frequency_analysis:
	python manage.py example_frequency_analysis "$(example)"

load_training_data:
	python manage.py load_training_data $(name) $(filepath) $(sheet_name)
