FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get -y install nginx

EXPOSE 8080

ADD . /
