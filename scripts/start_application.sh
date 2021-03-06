#!/usr/bin/env bash
cd /home/ubuntu/
cp -rf /home/ubuntu/forms/deploy /home/ubuntu/
chmod +x /home/ubuntu/deploy/deploy

sudo cp /home/ubuntu/forms/deploy/forms /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx

sudo cp /home/ubuntu/forms/deploy/forms.conf /etc/supervisor/conf.d/
sudo systemctl restart supervisor
sudo systemctl enable supervisor
sudo supervisorctl start forms
