GCC:= gcc

pub : publisher.o
	$(GCC) publisher.o -L/usr/local/lib /usr/local/lib/libmosquittopp.so.1 /usr/local/lib/libmosquitto.so.1 -o pub

publisher.o: publisher.c
	$(GCC) publisher.c -c
	
clean : 
	rm -f *.o pub
