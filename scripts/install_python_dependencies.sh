#!/usr/bin/env bash
chown ubuntu:ubuntu /home/ubuntu/forms
virtualenv /home/ubuntu/venv
chown ubuntu:ubuntu /home/ubuntu/venv
chown ubuntu:ubuntu /home/ubuntu/venv/*
source /home/ubuntu/venv/bin/activate
pip install -r /home/ubuntu/forms/requirements.txt
