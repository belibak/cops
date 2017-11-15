FROM alpine:3.5

RUN apk update &&\
	apk add python3 python3-dev py3-pip gcc g++ musl-dev linux-headers

RUN adduser -g "" -s /bin/sh -D white && chown white:white /var/log -R
ADD cops/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ADD cops /cops

RUN chown white:white /cops -R && apk del gcc g++ musl-dev linux-headers &&  cat /etc/passwd

ENTRYPOINT ["/bin/sh", "/cops/docker.sh"]
