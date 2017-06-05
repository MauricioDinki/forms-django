#!/usr/bin/env bash
cd /home/ubuntu/
source venv/bin/activate
cd forms
python manage.py makemigrations
python manage.py migrate
cd /home/ubuntu/
cp -rf /home/ubuntu/forms/deploy /home/ubuntu/
sudo cp /home/ubuntu/forms/deploy/forms /etc/nginx/sites-enabled
sudo systemctl restart nginx
sudo cp /home/ubuntu/forms/deploy/app.conf /etc/supervisor/conf.d/
sudo systemctl restart supervisor
sudo systemctl enable supervisor