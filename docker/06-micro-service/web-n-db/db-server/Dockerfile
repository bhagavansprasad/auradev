FROM ubuntu
FROM python

MAINTAINER bhagavan@auranetworks.in

#setting environment
ENV SRVR_PORT 80
ENV SRCPATH /home/bhagavan/auradev/docs/setup/nginx/source-files

#Install packages required
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install flask flask_restful

COPY db.py /usr/src

ENTRYPOINT python /usr/src/db.py $SRVR_PORT && bash

EXPOSE $SRVR_PORT





