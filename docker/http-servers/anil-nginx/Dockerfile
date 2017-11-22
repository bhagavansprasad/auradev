FROM nginx:latest
MAINTAINER bhagavan@auranetworks.in
ENV HTTP_PORT 80

RUN apt-get update
RUN apt-get install -y python2.7 fcgiwrap python-fcgi libfcgi0ldbl spawn-fcgi
RUN apt-get install -y wget dialog net-tools

RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled

COPY ./source-files/default /etc/nginx/sites-available
COPY ./source-files/nginx.conf /etc/nginx/nginx.conf
COPY ./source-files/fastcgi_params /etc/nginx/fastcgi_params
COPY ./source-files/fcgiwrap.default /etc/default/fcgiwrap

RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN mkdir -p /usr/share/nginx/html/cgi-bin

COPY ./source-files/env.cgi /usr/share/nginx/html/cgi-bin
COPY ./source-files/env.cgi /usr/share/nginx/html
COPY ./source-files/start_service.sh /

#RUN chmod g+rw /var/run/fcgiwrap.socket

#CMD service nginx start
#CMD service fcgiwrap start
#ENTRYPOINT ["service", "nginx", "start"]
#ENTRYPOINT ["service", "fcgiwrap", "start"]
#ENTRYPOINT ["/bin/sh", "-c", "while true; do sleep 1; done"]

#ENTRYPOINT service nginx restart && bash
#ENTRYPOINT service fcgiwrap restart && bash

ENTRYPOINT service nginx restart && service fcgiwrap restart && bash

EXPOSE $HTTP_PORT
