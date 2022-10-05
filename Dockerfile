# Dockerfile for Django Applications

# Section 1- Base Image
FROM python:alpine

# Section 2- Python Interpreter Flags
ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH="/usr/src/django_project/:$PYTHONPATH"
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# create the app user
RUN addgroup -S django_user && adduser -S django_user -G django_user

# set work directory
WORKDIR /usr/src/django_project

# install dependencies
RUN apk add --virtual build-deps gcc python3-dev musl-dev >/dev/null
RUN pip install --upgrade -q pip
COPY --chown=django_user:django_user ./requirements.txt .
RUN pip install --no-cache-dir -qr requirements.txt

RUN apk del build-deps >/dev/null

WORKDIR /usr/src/django_project

# copy project
COPY --chown=django_user:django_user . .

RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Change to non-root user
USER django_user

# Add execution permission for the start script
RUN chmod +x ./gunicorn.sh

# run gunicorn
CMD [ "/usr/src/django_project/gunicorn.sh"]