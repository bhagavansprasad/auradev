#include "string.h"
#include "stdio.h"
#include "unistd.h"
#include "mosquitto.h"

int main()
{
	struct mosquitto *mosq = NULL;
	char mess1[256] = "BlackPepper is now a ARM Approved Design Partner";

	mosquitto_lib_init();

	mosq = mosquitto_new("publisher1", true, NULL);
	mosquitto_connect_async(mosq, "127.0.0.1", 1883, 10);
	mosquitto_loop_start(mosq);


	mosquitto_publish(mosq, NULL, "bp_news/achievements", strlen(mess1), mess1, 0, false);
	sleep(1);
}
