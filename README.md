# Project Title

**Insert project description here**

The project is deployed on Heroku: [https://project-appname.herokuapp.com](https://project-appname.herokuapp.com)

The template project is deployed on Heroku: [https://cmps-453-project-template.herokuapp.com/](https://cmps-453-project-template.herokuapp.com/)

To develop this Django application, clone this repository and follow the instructions:

## What's Already Included in the Django Template?

-   User Authentication System:
    -   Login: [https://cmps-453-project-template.herokuapp.com/accounts/login/](https://cmps-453-project-template.herokuapp.com/accounts/login/)
    -   User Registration: [https://cmps-453-project-template.herokuapp.com/accounts/signup/](https://cmps-453-project-template.herokuapp.com/accounts/signup/)

## Install Python Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Collect Static Files

```bash
python manage.py collectstatic --no-input
```

## Run the Django Web Server

```bash
python manage.py runserver
```

## Developer's Guide

Before performing a `git push`, run these commands to ensure that the new code changes will pass
the pipeline stages:

### Python linting

**Pipeline Stage**: _lint_

To ensure code changes meet the python coding and documentation standards, run the following
commands:

```bash
pylama .
```

If the above command raises errors, fix the lines specified in the error messages.

### Django migrations

**Pipeline Stage**: _build_

To ensure Django migration files are created, applied, and added to git, run the following commands:

```bash
python manage.py makemigrations --check
python manage.py migrate --check
```

If the any of the above commands raises an error, create migration files and add to the commit.

### Django Tests

**Pipeline Stage**: _test_

To ensure code changes passes all unit tests, run the following commands:

```bash
python manage.py test
```

## Team Members

**Update the last name, first name, Heroku app name, and URLs in the table below **

| Role     | Last Name | First Name | Heroku App                                    |
| -------- | --------- | ---------- | --------------------------------------------- |
| Member A | Last Name | First Name | [heroku_app-a.herokuapp.com](update URL here) |
| Member B | Last Name | First Name | [heroku_app-b.herokuapp.com](update URL here) |
| Member C | Last Name | First Name | [heroku_app-c.herokuapp.com](update URL here) |
| Member D | Last Name | First Name | [heroku_app-d.herokuapp.com](update URL here) |

## Set up GitLab CD

See the [DEPLOY.md](DEPLOY.md)
