FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get -y install nginx

ADD . /app

ENV NOTIFY python /app/nginx-register.py
ENV INTERVAL 30

EXPOSE 8080
