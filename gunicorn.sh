#!/bin/sh
export NAME="Django Project Template" # Django application name
export DIR=/usr/src/django_project/   # Directory where project is located in the docker
export USER=django_user               # User to run this script as
export WORKERS=4                      # Number of workers that Gunicorn should spawn
export HOST=0.0.0.0
export PORT=8080
export DJANGO_WSGI_MODULE=django_project.wsgi # Which WSGI file should use
export LOG_LEVEL=info

python3 manage.py migrate

gunicorn ${DJANGO_WSGI_MODULE} \
    --preload \
    --reload \
    --chdir=$DIR \
    --user=$USER \
    --bind=$HOST:$PORT \
    --workers=$WORKERS \
    --log-level=$LOG_LEVEL
