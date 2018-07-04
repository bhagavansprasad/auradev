#include "stdio.h"

//#define DEBUG

main(int argc, char *argv[])
{
	int a = atoi(argv[1]);
	int retval;

#ifdef DEBUG
	printf("-->a value :%d\r\n", a);
#endif

	retval = is_prime(a);

#ifdef DEBUG
	printf("-->retval :%d\r\n", retval);
#endif

	if (retval)
		printf("%d is prime\r\n", a);
	else
		printf("%d is NOT prime\r\n", a);
}

int is_prime(int n)
{
	int i;

#ifdef DEBUG
	printf("-->In function %s n value :%d\r\n", __FUNCTION__, n);
#endif

	for (i = 2; i <= n; i++)
	{
#ifdef DEBUG
		printf("-->In loop i value:%d\r\n", i);
#endif

		if (n%i == 0)
		{
#ifdef DEBUG
			printf("-->n MOD i value :%d\r\n", n%i);
#endif
			break;
		}
	}

	if (i == n)
	{
#ifdef DEBUG
		printf("-->returning 1 from %s, because number is prime\r\n", __FUNCTION__);
#endif
		return 1;
	}
	else
	{
#ifdef DEBUG
		printf("-->returning 0 from %s, because number is NOT prime\r\n", __FUNCTION__);
#endif
		return 0;
	}
}
