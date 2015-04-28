
# List of Environment Variables

## Server
* SERVER_NAME : Nginx 'server_name' directive. ('_')

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
