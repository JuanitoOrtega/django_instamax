#!/bin/bash

DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
DJANGO_SETTINGS_MODULE=a_core.settings
cd $DJANGODIR
source /home/jogman/.pyenv/versions/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
exec python manage.py runserver 0:8000
