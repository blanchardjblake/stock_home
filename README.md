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

### Visual Studio Code

It's highly recommended to use [VSCode](https://code.visualstudio.com/) to develop the Django project.

The project repository comes with VSCode-specific settings that make the development much more effortless.

While importing the project into the VSCode, open the root folder of the project such that VSCode can
read the [.vscode/settings.json](.vscode/settings.json) file.

If you're using a python virtual env for this project and the `.venv` or `venv` folder is in the root
folder of the repository, then VSCode automatically identifies the virtual env. Otherwise, press
`CTRL + SHIFT + P` and search for `python: select interpreter` and specify the path to the installation
path of the python virtual env on your machine.

Upon opening the project folder onto the VSCode, install all extensions
([.vscode/extensions.json](.vscode/extensions.json)) recommended by the project's settings.

-   [esbenp.prettier-vscode](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
-   [monosans.djlint](https://marketplace.visualstudio.com/items?itemName=monosans.djlint)
-   [ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
-   [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [njpwerner.autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
-   [zhuangtongfa.material-theme](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)
-   [Gitlab.gitlab-workflow](https://marketplace.visualstudio.com/items?itemname=gitlab.gitlab-workflow)

These extensions require specific pip packages to be installed.

The [requirements.txt](requirements.txt) file includes the pip packages required for the VSCode extensions.

That's why VSCode needs to know the python virtual environment of the Django project for the normal
functioning of the recommended extensions.

### GitLab CI/CD pipelines

Before performing a `git push`, run these commands to ensure that the new code changes passes
the pipeline stages:

#### Python linting

**Pipeline Stage**: _lint_

To ensure code changes meet the python coding and documentation standards, run the following
commands:

```bash
pylama .
```

If the above command raises errors, fix the lines specified in the error messages.

#### Django migrations

**Pipeline Stage**: _build_

To ensure Django migration files are created, applied, and added to git, run the following commands:

```bash
python manage.py makemigrations --check
python manage.py migrate --check
```

If the any of the above commands raises an error, create migration files and add to the commit.

#### Django Tests

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

## (Optional) Develop the project using Docker

Install [docker engine](https://docs.docker.com/engine/install/) and
[docker-compose](https://docs.docker.com/compose/install/).

The [docker-compose.dev.yml](docker-compose.dev.yml) is configured to mount the current working
directory (the repository's root) inside the docker container.

It enables editing changes on your machine using VSCode, and the Django running inside the docker
container reloads the changes automatically.

### Build

From the root of this repository, run the following command:

```bash
docker-compose -f docker-compose.dev.yml build
```

The above command builds two docker images—one with the Django project and the other with the `PostgreSQL` DB.

### Run

```bash
docker-compose -f docker-compose.dev.yml up
```

The above command brings the docker container to a running stage.

Open the browser and visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

### Stop

To shutdown down all the dockers safely, run the following command:

```bash
docker-compose -f docker-compose.dev.yml down --remove-orphans
```
