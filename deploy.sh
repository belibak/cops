#!/bin/bash
sudo apt-get update && sudo apt-get install virtualenv python3 supervisor nginx
virtualenv --python=python3 venv
venv/bin/pip install -r requirements.txt

