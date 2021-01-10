# django-project-template

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

## Set up GitLab continuous delivery

We will use GitLab CI/CD for continuous deployment on Heroku which is a platform as a service
that enables developers to build, run, and operate application entirely on cloud.

### Create an account on Heroku

To start using Heroku you will first need to create an account:

1. Go to https://www.heroku.com and click the `SIGN UP FOR FREE` button.
2. Enter your details and then press `CREATE FREE ACCOUNT`.
    You'll be asked to check your account for a sign-up email.
3. Click the account activation link in the signup email.
    You'll be taken back to your account on the web browser.
4. Enter your password and click `SET PASSWORD AND LOGIN`.
5. You'll then be logged in and taken to the Heroku dashboard: https://dashboard.heroku.com/apps.

To view the `API Key` of your account, visit `Account Settings` and click on the `Reveal` button.

### Create an app on Heroku
On your Heroku account, click on `New` > `Create new app`, name it `heroku-gitlab-staging`.

### Set up GitLab CD variables
On your GitLab project repository, visit `settings` > `CI/CD`, and click on `Expand` button of the `Variables`.

Add the below two variables and uncheck masked and protected flags:
1. Key: `HEROKU_API_KEY`, Value: `API key` from Heroku `Account Settings`
2. Key: `HEROKU_APP_STAGING`, Value: `heroku-gitlab-staging` name of the app that you have created on Heroku.

Click on `Save variables` once you have added both variables.

### Activate delivery when the the GitLab pipeline is triggered
Append the below lines to the `.gitlab-ci.yml` at the end of the file:

```yaml
staging:
    stage: deploy
    before_script:
        - apt-get update -qy
        - apt-get install -y ruby-dev
        - gem install dpl
    script:
        - dpl --provider=heroku --app=$HEROKU_APP_STAGING --api-key=$HEROKU_API_KEY --run='python manage.py migrate'
```

