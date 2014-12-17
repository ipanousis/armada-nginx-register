FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get -y install nginx

ADD . /app

ENV NOTIFY python /app/nginx-register.py

EXPOSE 8080
