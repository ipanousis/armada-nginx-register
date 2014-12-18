FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get -y install nginx

ADD . /

ENV NOTIFY python /nginx-register.py ; /etc/init.d/nginx configtest && /etc/init.d/nginx reload

EXPOSE 8080
