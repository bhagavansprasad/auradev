pub : pub_cloud.o
	g++ pub_cloud.o -L/usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/libmosquitto.so.1 -o pub

pub_cloud.o: pub_cloud.c
	g++ pub_cloud.c -c
	
clean : 
	rm -f *.o pub
