test:
	python manage.py test

server:
	python manage.py runserver

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=laboratory/asgi.py,laboratory/wsgi.py,manage.py --fail-under=100
	coverage html --omit=laboratory/asgi.py,laboratory/wsgi.py,manage.py