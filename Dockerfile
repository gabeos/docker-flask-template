
FROM phusion/baseimage

MAINTAINER Gabriel Schubiner <g@gabeos.cc>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install \
    nginx \
    python-pip \
    python-dev \
    libpq-dev \
    libmysqlclient-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ONBUILD COPY requirements.txt /var/www/flask/requirements_additional.txt
ONBUILD RUN pip install -r /var/www/flask/requirements_additional.txt

COPY flask.nginx.conf /etc/nginx/sites-available/
RUN rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.nginx.conf /etc/nginx/sites-enabled/flask.conf

RUN mkdir -p /var/log/uwsgi /var/log/flask && \
    touch /var/log/uwsgi/flask.log /var/log/flask/flask.log

COPY flask /var/www/flask/
RUN pip install -r /var/www/flask/requirements.txt

COPY run/init.run /etc/my_init.d/10_init
COPY run/lf.nginx.run /etc/service/nginx-log-forwarder/run
COPY run/lf.flask.run /etc/service/flask-log-forwarder/run
COPY run/lf.uwsgi.run /etc/service/uwsgi-log-forwarder/run
COPY run/nginx.run /etc/service/nginx/run
COPY run/uwsgi.run /etc/service/uwsgi/run

WORKDIR /var/www/flask

EXPOSE 80
VOLUME /var/www/flask
CMD ["/sbin/my_init"]

