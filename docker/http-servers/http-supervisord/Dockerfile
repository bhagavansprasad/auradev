FROM nginx:latest
MAINTAINER bhagavan@auranetworks.in
ENV HTTP_PORT 80

RUN apt-get update
RUN apt-get install -y python2.7 fcgiwrap python-fcgi libfcgi0ldbl
RUN apt-get install -y net-tools
RUN apt-get install -y supervisor
RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled

COPY ./source-files/default /etc/nginx/sites-available
COPY ./source-files/nginx.conf /etc/nginx/nginx.conf
COPY ./source-files/fastcgi_params /etc/nginx/fastcgi_params
COPY ./source-files/fcgiwrap.default /etc/default/fcgiwrap
COPY ./source-files/supervisord.conf /etc/

RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN mkdir -p /usr/share/nginx/html/cgi-bin

COPY ./source-files/env.cgi /usr/share/nginx/html/cgi-bin
COPY ./source-files/env.cgi /usr/share/nginx/html
COPY ./source-files/start_service.sh /

EXPOSE $HTTP_PORT

CMD ["/usr/bin/supervisord"]
