FROM ubuntu
FROM gcc
MAINTAINER bhagavan
 
ENV PORT 8888

COPY tcpechoserver.c /usr/src/tcpechoserver/tcpechoserver.c

WORKDIR /usr/src/tcpechoserver

RUN gcc -o /usr/bin/myechoserver /usr/src/tcpechoserver/tcpechoserver.c

CMD /usr/bin/myechoserver $PORT

EXPOSE $PORT

