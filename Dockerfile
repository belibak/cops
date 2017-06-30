FROM python:3.5 

RUN adduser white --shell /bin/bash --disabled-password --gecos "" && chown white:white /var/log -R

ADD cops /cops

RUN pip install -r /cops/requirements.txt

CMD ["/bin/bash", "/cops/docker.sh"]

EXPOSE 80
