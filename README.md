
# Flask Template in Docker

## What is this?

A fully configured and ready to hack flask template loaded up with Bootstrap 3, jQuery, and a bunch of Flask Extensions, served via nginx and uWSGI.

All credit for the actual Flask app implementation and design goes to Steven Loria (@sloria) and his project cookiecutter-flask.
This Dockerfile basically just wraps that up into a container, removes some unnecessaries and replaces gunicorn with uWSGI.

Head over to [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask) to learn more about the contained app.

## Docs

### Environment Variables



# Environment Variables

| Section | Variable Name | Default | Details |
| --- | --- | --- | --- | 
| Server | --- | --- | --- |
| --- | SERVER_NAME | '_' | Nginx 'server_name' directive. |

## Mail

* MAIL_SERVER
* MAIL_PORT
* MAIL_TLS
* MAIL_SSL
* MAIL_USER
* MAIL_PASS
* MAIL_SENDER

## DB

Use linked postgres or mysql/mariadb container for automated db configuration.
Otherwise use DB_URI or DB_*. DB_URI takes precedence:

* DB_URI : Specify whole URI in one environment variable
* DB_USER 
* DB_PASS
* DB_ADDR
* DB_PORT
* DB_TYPE : Optional if DB port is standard mysql (3306) or postgres (5432) port

## Flask
* CREATE_FLASK_DB : use `python manage.py ...` commands to make databases with SQLAlchemy. Defaults to `false`. Set to `true` to enable.

## User Info
* PROJECT_NAME : Name you would like to show up in the templates
* USER_EMAIL : Email to provide in the `contact` link (`mailto:$USER_EMAIL`)
