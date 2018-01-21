#!/usr/bin/env bash
python manage.py migrate
python manage.py collectstatic
uwsgi uwsgi.ini
exec $@