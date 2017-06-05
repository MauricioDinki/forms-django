#!/usr/bin/env bash

NAME="forms"
VIRTUALENV="/home/ubuntu/venv"
DJANGO_DIR="/home/ubuntu/forms"
USER=root
GROUP=sudo
NUM_WORKERS=5
DJANGO_WSGI_MODULE=forms.wsgi

echo "Starting $NAME as `whoami`"

cd $VIRTUALENV
source bin/activate
cd $DJANGO_DIR

exec gunicorn ${DJANGO_WSGI_MODULE} \
        --bind=0.0.0.0:8000 \
        --workers $NUM_WORKERS
