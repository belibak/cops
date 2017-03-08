FROM ubuntu:latest

RUN adduser white --shell /bin/bash --disabled-password --gecos "" && chown white:white /var/log -R

RUN apt-get update&& apt-get -y install\
  python3\
  virtualenv\
  supervisor

ADD cops /cops

RUN virtualenv --python=python3 /venv
RUN /venv/bin/pip install -r /cops/requirements.txt

#RUN cp /cops/docker-confs/nginx.cops.conf /etc/nginx/sites-enabled/default\
#  && cp /cops/docker-confs/supervisor.* /etc/supervisor/conf.d/
#
#RUN update-rc.d supervisor enable && update-rc.d nginx enable

CMD ["/bin/bash", "/cops/docker.sh"]

EXPOSE 80
