#!/usr/bin/env bash
sudo chown ubuntu:ubuntu /home/ubuntu/forms
virtualenv /home/ubuntu/venv
sudo chown ubuntu:ubuntu /home/ubuntu/venv
sudo chown ubuntu:ubuntu /home/ubuntu/venv/*
sudo chown ubuntu:ubuntu /home/ubuntu/.aws/*
source /home/ubuntu/venv/bin/activate
pip install -r /home/ubuntu/forms/requirements.txt
