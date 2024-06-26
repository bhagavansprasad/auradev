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
		//sprintf(mess1, "Message #%d Hi 0", i);
		sprintf(mess2, "Message #%d Bye 1", i);

		//mosquitto_publish(mosq, NULL, "topic1/a/b/c", strlen(mess1), mess1, 0, false);
		mosquitto_publish(mosq, NULL, "topic2/a/b/c", strlen(mess2), mess2, 1, false);
		sleep(1);
		//break;
	}
}
