FROM ubuntu
FROM gcc
MAINTAINER bhagavan
 
ENV PORT 8888

COPY tcpechoserver.c /usr/src/tcpechoserver/tcpechoserver.c
WORKDIR /usr/src/tcpechoserver

CMD mkdir /tmp/llibs
RUN gcc -c tcpechoserver.c -o /tmp/llibs/myechoserver.o
RUN gcc /tmp/llibs/myechoserver.o -o tcpechoserver

CMD myechoserver $PORT

EXPOSE $PORT

