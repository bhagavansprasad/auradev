FROM ubuntu
FROM gcc4.9
MAINTAINER bhagavan

ENV PORT 8888
COPY tcpechoserver.c /tmp
CMD gcc /tmp/tcpechoserver.c -o /usr/bin/my_tcp_echo.out
CMD /usr/bin/my_tcp_echo.out $PORT

EXPOSE $PORT

