run-dev:
	python ./manage.py runserver

makemigrations:
	python ./manage.py makemigrations

migrate:
	python ./manage.py migrate

startapp:
	django-admin startapp $(name)