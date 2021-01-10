# django-project-template

A Django project template with CI, gitignore, README, development, and deployment instructions

To develop/test this website, clone this repository and follow the instructions:

## Install Python requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Set the environment variables

For development, enable two environment variables: `DEBUG` and `SECRET_KEY`.

### Enable the debug mode for development

`DEBUG` is disabled by default. To enable it, set the environment variable:

```bash
export DEBUG=True
```

### Set a secret key for the development

1. Generate a secret key using the following command:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

2. Set the generated secret key as an environment variable:

```bash
export SECRET_KEY='NEW_KEY_GENERATED_IN_STEP1'
```

## Run the test webserver
```bash
python manage.py runserver
```
