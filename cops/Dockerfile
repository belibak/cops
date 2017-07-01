FROM ubuntu:latest

RUN adduser white --shell /bin/bash --disabled-password --gecos "" && chown white:white /var/log -R

RUN apt-get update&& apt-get -y install\
  python3\
  virtualenv\
  supervisor

ADD python /cops

RUN virtualenv --python=python3 /venv &&

RUN ls /cops -alh
RUN cp /cops/docker-confs/nginx.* /etc/nginx/sites-enabled/\
  && cp /cops/docker-confs/supervisor.* /etc/supervisor/conf.d/

RUN update-rc.d supervisor enable

CMD ['/venv/bin/python','/cops/run.py']

EXPOSE 80
