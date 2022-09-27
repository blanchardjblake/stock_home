release: python manage.py migrate
web: gunicorn django_project.wsgi --workers 2 --max-requests 1200 --preload --timeout 10 --log-file -
