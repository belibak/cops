#!/bin/sh

chown white:white /volume -R
cd /cops && uwsgi --ini uwsgi.ini

