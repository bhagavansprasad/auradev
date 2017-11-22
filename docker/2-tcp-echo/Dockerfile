FROM ubuntu
FROM gcc
MAINTAINER bhagavan

ENV PORT 8888
COPY tcpechoserver.c /tmp
RUN gcc /tmp/tcpechoserver.c -o /usr/bin/my_tcp_echo.out
CMD /usr/bin/my_tcp_echo.out $PORT

EXPOSE $PORT

