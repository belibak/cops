FROM python:3.5

RUN adduser white --shell /bin/bash --disabled-password --gecos "" && chown white:white /var/log -R
ADD cops/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD cops /cops

CMD ["/bin/bash", "/cops/docker.sh"]

EXPOSE 80
