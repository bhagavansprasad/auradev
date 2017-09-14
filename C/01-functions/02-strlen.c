#include "stdio.h"

int astrlen()
{
	for (i = 0; sname[i] != '\0'; i++)
		printf("%c", sname[i]);


}

main()
{
	char sname[100] = "Aura Networks Bng";
	int i = 0;

	printf("sname :%s\n", sname);

	for (i = 0; sname[i] != '\0'; i++)
		printf("%c", sname[i]);


	printf("\n");
	printf("len of the string is :%d\n", i);
}
