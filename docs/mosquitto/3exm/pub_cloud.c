#include "string.h"
#include "stdio.h"
#include "unistd.h"
#include "mosquitto.h"

int main()
{
	struct mosquitto *mosq = NULL;
	int i = 0;
	char mess1[256];
	char mess2[256];

	mosquitto_lib_init();

	mosq = mosquitto_new("publisher1", true, NULL);
	mosquitto_connect_async(mosq, "test.mosquitto.org", 1883, 10);
	mosquitto_loop_start(mosq);

	for ( ;  ; i++)
	{
		sprintf(mess2, "{\"version\":\"1.0.0\",\"vin\":\"car1\",\"datastreams\":[{\"id\":\"DistPub\",\"current_value\":\"6070635\"}]}");

		mosquitto_publish(mosq, NULL, "aura_net_recru/a/b/c", strlen(mess2), mess2, 1, false);
		sleep(1);
	}
}
