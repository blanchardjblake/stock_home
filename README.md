# Stock Home

**The Stock Home provides users free, easy access to real time stock data. Uses can view graphical representation of stock price history for the past day, week, month, six months, year, or five years. Additionally, users can view tabular data containing stock attributes such as yearly dividend yield, current day opening price, current day min/max price, & previous year min/max price.
Without an account, users can only view stock data, but creating an account gives users purchase options. Upon creating an account, users are instructed to view basic trading documentation included on the site. Until completing the review, users will be denied access to trading even with an account.
Our site provides an easily accessible, commission-free trading platform to enable users of all financial backgrounds to participate in the market & attempt to grow their wealth. Additionally, the provided stock trading knowledge base will help prevent reckless trading among newcomers & increase the number of educated traders in the market.**

The project is deployed on Heroku:
[https://fa22-team-d.herokuapp.com/](https://fa22-team-d.herokuapp.com/)

To develop the Django application, clone this repository and follow the instructions:

## What's Already Included in the Django Template?

-   User Authentication System:
    -   [Login](https://fa22-team-d.herokuapp.com/accounts/login/)
    -   [User Registration](https://cmps-453-project-template.herokuapp.com/accounts/signup/)

## Create Python Virtual Environment

```bash
virtualenv --python=/usr/bin/python3 .venv  # for UNIX and MacOS bash/zsh
```

```bash
python -m virtualenv .venv                  # for Windows git bash and Windows CMD
```

## Activate Python Virtual Environment

```bash
source .venv/bin/activate                   # for UNIX and MacOS bash/zsh
```

```bash
source .venv/Scripts/activate               # for Windows git bash
```

```cmd
.venv\Scripts\activate.bat                  # for Windows CMD
```

For the following steps and for development, keep the virtual environment activated all the time.

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

It's highly recommended to use [VSCode](https://code.visualstudio.com/) for the development.

The project repository includes VSCode-specific settings ([.vscode/settings.json](.vscode/settings.json))
that are helpful for developing Django applications.

With the python virtual environment active, from the root of the repository,
open the VSCode using the following command:

```bash
code .
```

Please install all the extensions (specified in [.vscode/extensions.json](.vscode/extensions.json))
recommended by VSCode upon opening the project in the code editor.

The [requirements.txt](requirements.txt) file includes the python packages required for some
of the VScode extensions. That's why VSCode needs to be opened from the bash or command
line with an active python virtual environment in which all the project-specific python packages
are installed.

Some fonts to reduce eye strain and provide better coding experience:

-   [FiraCode](https://github.com/tonsky/FiraCode)
-   [Jet Brains Mono](https://github.com/JetBrains/JetBrainsMono)
-   [Hack](https://github.com/source-foundry/Hack)

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
| Member A | Blanchard | Blake      | https://fa22-team-d-a.herokuapp.com/          |
| Member B | Ho        | Nicholas   | https://fa22-team-d-b.herokuapp.com/          |
| Member C | Russell   | Nicholas   | https://fa22-team-d-c.herokuapp.com/          |
| Member D | Trahan    | Gabriel    | https://fa22-team-d-d.herokuapp.com/          |

## (Optional) Use Docker Containers for Development

See [DOCKER.md](DOCKER.md) file.
