pub : pub_cloud.o
	g++ pub_cloud.o  -L/usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/libmosquitto.so.1 -o pub1
	g++ pub_cloud2.o -L/usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/libmosquitto.so.1 -o pub2

pub_cloud.o: pub_cloud.c
	g++ pub_cloud.c -c
	g++ 2pub_cloud.c -c -o pub_cloud2.o
	
clean : 
	rm -f *.o pub pub2
