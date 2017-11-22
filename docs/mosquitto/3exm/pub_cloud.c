#include "string.h"
#include "stdio.h"
#include "unistd.h"
#include "mosquitto.h"

int main()
{
	struct mosquitto *mosq = NULL;
	int i = 1;
	char mess[256];

	mosquitto_lib_init();

	mosq = mosquitto_new("publisher", true, NULL);
	//mosquitto_connect_async(mosq, "test.mosquitto.org", 1883, 10);
	mosquitto_connect_async(mosq, "localhost", 1883, 10);
	mosquitto_loop_start(mosq);

	for ( ;  ; i++)
	{
		sprintf(mess, "{%d.Message from Aura}", i);
		printf("%d.Sending message...%s\n", i, mess);
		mosquitto_publish(mosq, NULL, "auranetworks", strlen(mess), mess, 1, false);
		sleep(1);
	}
}
