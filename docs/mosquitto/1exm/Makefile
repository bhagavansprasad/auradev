pub : publisher.o
	g++ publisher.o -L/usr/local/lib /usr/local/lib/libmosquittopp.so.1 /usr/local/lib/libmosquitto.so.1 -o pub

publisher.o: publisher.c
	g++ publisher.c -c
	
clean : 
	rm -f *.o pub
