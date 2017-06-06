#!/usr/bin/env bash
cd /home/ubuntu/
source venv/bin/activate
cd forms
cp mv enviroment .env
python manage.py makemigrations
python manage.py migrate
