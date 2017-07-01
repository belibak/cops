#!/bin/bash

#python /cops/run.py
cd /cops/cops && uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app


#service supervisor start
#service nginx start
#tail -f /var/log/*
