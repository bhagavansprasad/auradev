PORT=5000

tcpechoserver: tcpechoserver.c
	gcc tcpechoserver.c -o my_tcpechoserver
clean:
	rm my_tcpechoserver
run: tcpechoserver
	./my_tcpechoserver ${PORT}
test:
	printf "hello" | nc localhost ${PORT}
