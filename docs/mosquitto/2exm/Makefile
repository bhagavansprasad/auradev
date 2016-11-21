pub : pub_cloud.o
	#g++ pub_cloud.o -L/usr/local/lib /usr/local/lib/libmosquittopp.so.1 /usr/local/lib/libmosquitto.so.1 -o pub
	#g++ pub_cloud.o -L/usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/libmosquittopp.so.1 /usr/lib/x86_64-linux-gnu/libmosquitto.so.1 -o pub
	g++ pub_cloud.o -L/usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/libmosquitto.so.1 -o pub
	
clean : 
	-rm -f *.o pub
