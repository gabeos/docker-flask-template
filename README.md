
# Flask Template in Docker

## What is this?

A fully configured and ready to hack flask template loaded up with Bootstrap 3, jQuery, and a bunch of Flask Extensions, served via nginx and uWSGI.

All credit for the actual Flask app implementation and design goes to Steven Loria (@sloria) and his project cookiecutter-flask.
This Dockerfile basically just wraps that up into a container, removes some unnecessaries and replaces gunicorn with uWSGI.

Head over to [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask) to learn more about the contained app.

## Docs

### Database

Use linked postgres or mysql/mariadb container for automated db configuration. 
See fig.yml in repo for example.

Otherwise use DB_URI or DB_*. DB_URI takes precedence:

## Environment Variables

| Section | Variable Name | Default | Details |
| --- | --- | --- | --- | 
| Server | | | |
| | SERVER_NAME | '_' | Nginx 'server_name' directive. |
| Mail | | | |
| | MAIL_SERVER | | SMTP server |
| | MAIL_PORT | 587 | Port |
| | MAIL_TLS | true | Use TLS for communication with mail server |
| | MAIL_SSL | false | Use SSL for communication with mail server |
| | MAIL_USER | admin | Login username for SMTP server |
| | MAIL_PASS | | Login password for SMTP server |
| | MAIL_SENDER | admin@example.com | Email address to send mail from |
| DB | | | |
| | DB_URI | | Specify whole URI in one environment variable |
| | DB_USER | | Login user for DB |
| | DB_PASS | | Password for user@db |
| | DB_ADDR | | domain or IP of DB |
| | DB_PORT | | Port of DB |
| | DB_TYPE | | Type of database, 'mysql' or 'postgresql'. Optional if DB port is standard mysql (3306) or postgres (5432) port |

## Flask
* CREATE_FLASK_DB : use `python manage.py ...` commands to make databases with SQLAlchemy. Defaults to `false`. Set to `true` to enable.

## User Info
* PROJECT_NAME : Name you would like to show up in the templates
* USER_EMAIL : Email to provide in the `contact` link (`mailto:$USER_EMAIL`)
