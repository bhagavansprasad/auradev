#FROM ubuntu
#FROM gcc:4.9
#MAINTAINER bhagavan
#
#ENV PORT 8888
#COPY tcpechoserver.c /tmp
#WORKDIR /tmp
#RUN gcc tcpechoserver.c -o /usr/bin/my_tcp_echo
#CMD /usr/bin/my_tcp_echo $PORT
#
#EXPOSE $PORT
#

FROM ubuntu
FROM gcc:4.9
MAINTAINER bhagavan
 
ENV PORT 8888

COPY tcpechoserver.c /usr/src/tcpechoserver/tcpechoserver.c

WORKDIR /usr/src/tcpechoserver

RUN gcc -o /usr/bin/myechoserver /usr/src/tcpechoserver/tcpechoserver.c

CMD /usr/bin/myechoserver $PORT

EXPOSE $PORT

