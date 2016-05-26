pub : pub_cloud.o
	g++ pub_cloud.o -L/usr/local/lib /usr/local/lib/libmosquittopp.so.1 /usr/local/lib/libmosquitto.so.1 -o pub

pub_cloud.o: pub_cloud.c
	g++ pub_cloud.c -c
	
clean : 
	-rm -f *.o pub
