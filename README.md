# Django Project Template

A Django project template with CI, gitignore, README, development, and deployment instructions

To develop/test this website, clone this repository and follow the instructions:

## Install Python requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python django_project/manage.py migrate
```

## Set the environment variables

For development, enable two environment variables: `DEBUG` and `SECRET_KEY`.

### Enable the debug mode for development

`DEBUG` is disabled by default. To enable it, set the environment variable:

(For Linux and Mac only)
```bash
export DEBUG=True
```

(for Windows only)
```bash
set DEBUG=True
```

### Set a secret key for the development

1. Generate a secret key using the following command:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

2. Set the generated secret key as an environment variable:

(For linux and Mac only)
```bash
export SECRET_KEY='NEW_KEY_GENERATED_IN_STEP1'
```

(For Windows CMD only)
```
set SECRET_KEY='NEW_KEY_GENERATED_IN_STEP1'
```

These variables needs to be set everytime before you start running the development server.

The best practice would be to add these variables to your current user's environment
variable set registery (on Windows) or `$HOME/.bashrc` file (for Linux and Mac).

## Run the test webserver
```bash
python django_project/manage.py runserver
```

## Set up GitLab CD

See the [DEPLOY.md](DEPLOY.md)
