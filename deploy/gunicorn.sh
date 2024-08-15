#!/bin/bash

NAME='django_instamax'
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/django_instamax.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
NUM_WORKERS=4
DJANGO_WSGI_MODULE=a_core.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec /home/jogman/.pyenv/versions/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
