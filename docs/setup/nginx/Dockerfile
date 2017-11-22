FROM nginx:latest
MAINTAINER bhagavan@auranetworks.in
ENV HTTP_PORT 80
RUN apt-get update
RUN apt-get install -y python2.7 fcgiwrap python-fcgi libfcgi0ldbl spawn-fcgi
RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled
COPY ./source-files/default /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN mkdir -p /usr/share/nginx/html/cgi-bin
COPY ./source-files/env.cgi /usr/share/nginx/html/cgi-bin
COPY ./source-files/env.cgi /usr/share/nginx/html

EXPOSE $HTTP_PORT
