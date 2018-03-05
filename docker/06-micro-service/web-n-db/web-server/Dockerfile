FROM ubuntu
FROM python

MAINTAINER bhagavan@auranetworks.in

#setting environment
ENV HTTP_PORT 80
ENV SRCPATH /home/bhagavan/auradev/docs/setup/nginx/source-files

#Install packages required
RUN apt-get update
RUN apt-get install -y nginx fcgiwrap php5-fpm python-fcgi libfcgi0ldbl

#copy configuration files

COPY nginx.conf /etc/nginx/
COPY index.html /usr/share/nginx/html/
COPY index.php /usr/share/nginx/html/
COPY default /etc/nginx/sites-available
RUN mkdir -p /usr/share/nginx/html/cgi-bin
COPY env.cgi /usr/share/nginx/html/cgi-bin

#Restart services
ENTRYPOINT service nginx restart && service fcgiwrap restart && service php5-fpm restart && bash

EXPOSE $HTTP_PORT





