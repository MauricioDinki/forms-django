#!/usr/bin/env bash
cd /home/ubuntu/
source venv/bin/activate
cd forms
python manage.py makemigrations
python manage.py migrate
cd /home/ubuntu/
cp -rf /home/ubuntu/forms/deploy /home/ubuntu/
