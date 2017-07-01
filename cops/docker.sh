#!/bin/bash

cd /cops && uwsgi --ini uwsgi.ini

#service supervisor start
#service nginx start
#tail -f /var/log/*
