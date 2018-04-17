FROM alpine:3.7

RUN apk update &&\
	apk add python3 python3-dev py3-pip gcc g++ musl-dev linux-headers

RUN adduser -g "" -s /bin/sh -D white && chown white:white /var/log -R
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --default-timeout=100 -r /tmp/requirements.txt
RUN pip3 install uwsgi
