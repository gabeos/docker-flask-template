# -*- config:utf-8 -*-

import logging, os
from datetime import timedelta

# base config class; extend it to your needs.
class Config(object):

    def __get_db_type_from_port():
        if os.environ['DB_PORT'] == '5432':
            os.getenv('DB_TYPE','postgresql')
        elif os.environ['DB_PORT'] == '3306':
            os.getenv('DB_TYPE','mysql')
        else:
            os.getenv('DB_TYPE','postgresql')

    def __get_db_uri_from_env():
        if os.environ.get('DB_PORT_5432_TCP'):
            userdb = os.getenv('DB_ENV_POSTGRES_USER','postgres')
            dbpass = os.environ.get('DB_ENV_POSTGRES_PASSWORD')
            dbaddr = os.getenv('DB_PORT_5432_TCP_ADDR')
            return "postgresql://%s:%s@%s/%s" % (userdb, dbpass, dbaddr, userdb)
        elif os.environ.get('DB_PORT_3306_TCP'):
            dbuser = os.getenv('DB_ENV_MYSQL_USER','root')
            dbpass = os.environ.get('DB_ENV_MYSQL_PASSWORD', os.getenv('DB_ENV_MYSQL_ROOT_PASSWORD','mysql'))
            dbaddr = os.getenv('DB_PORT_3306_TCP_ADDR')
            dbdb   = os.getenv('DB_ENV_MYSQL_DATABASE','flask')
            return "mysql://%s:%s@%s/%s" % (userdb, dbpass, dbaddr, dbdb)
        elif os.environ.get('DB_URI'):
            return os.environ['DB_URI']
        elif os.environ.get('DB_PORT'):
            dbuser = os.getenv('DB_USER','flask')
            dbpass = os.getenv('DB_PASS','flask')
            dbaddr = os.getenv('DB_ADDR','localhost')
            dbdb   = os.getenv('DB_NAME','flask')
            dbtype = self.__get_db_type_from_port()
            return "%s://%s:%s@%s/%s" % (dbtype, userdb, dbpass, dbaddr, dbdb)
        else:
            return "sqlite:////var/www/flask/app.db"

    def __get_blueprints_from_env():
        if os.environ.get('BLUEPRINTS'):
            return os.environ['BLUEPRINTS'].split(',')
        else: 
            return ['blog']

    ENV = "prod"

    # use DEBUG mode?
    DEBUG = False

    # use TESTING mode?
    TESTING = False

    # use server x-sendfile?
    USE_X_SENDFILE = False

    # DATABASE CONFIGURATION
    # see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = __get_db_uri_from_env()
    SQLALCHEMY_ECHO = False

    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']

    # LOGGING
    LOGGER_NAME = "%s_log" % app
    LOG_FILENAME = "/var/log/flask/flask.log"
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s" # used by logging.Formatter

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # EMAIL CONFIGURATION
    MAIL_SERVER = os.getenv("MAIL_SERVER","localhost")
    MAIL_PORT = os.getenv("MAIL_PORT","587")
    MAIL_USE_TLS = os.getenv("MAIL_TLS","true") == "true"
    MAIL_USE_SSL = os.getenv("MAIL_SSL", "true") == "true"
    MAIL_DEBUG = False
    MAIL_USERNAME = os.getenv("MAIL_USER","admin")
    MAIL_PASSWORD = os.getenv("MAIL_PASS","admin")
    DEFAULT_MAIL_SENDER = os.getenv("MAIL_SENDER","example@example.com" % )

    # see example/ for reference
    # ex: BLUEPRINTS = ['blog']  # where app is a Blueprint instance
    # ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where app is a Blueprint instance
    BLUEPRINTS = __get_blueprints_from_env()

# config class for development environment
class DevConfig(Config):
    ENV = "dev"
    DEBUG = True  # we want debug level output
    MAIL_DEBUG = True
    SQLALCHEMY_ECHO = True  # we want to see sqlalchemy output
    SQLALCHEMY_DATABASE_URI = "sqlite:////var/tmp/app_dev.sqlite"


# config class used during tests
class Test(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/app_test.sqlite"
