#include "string.h"
#include "stdio.h"

int astrlen(char *pname)
{
	int i = 0;

	for (i = 0; pname[i] != '\0'; i++)
	{
	}

	return i;
}

int astrcpy(char *d, char *s)
{
}

main()
{
	char s1[] = "Hello How are you";
	char s2[100];

	int i = 0, retval  = 0;

	for (i = 0; s1[i] != '\0'; i++)
	{
	}

	printf ("len    :%d\n", i);
	printf ("strlen :%d\n", (int)strlen(s1));

	retval = astrlen(s1);
	printf ("retval :%d\n", retval);

	printf ("s1 :%s\n", s1);
	printf ("s2 :%s\n", s2);
	//strcpy(s2, s1);
	astrcpy(s2, s1);
	printf ("s1 :%s\n", s1);
	printf ("s2 :%s\n", s2);
}


