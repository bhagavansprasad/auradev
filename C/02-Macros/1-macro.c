
#define GET_PRODUCT(x, y, z) ((z) = (x) * (y))

main()
{
	int a = 5, b = 6, c = 0;
	char *p = malloc(-10);
	printf("%p\n", p);

	printf("1. c = %d * %d     :%d\n", a, b, GET_PRODUCT(a, b, c));
	printf("2. c = %d+2 * %d+5 :%d\n", a, b, GET_PRODUCT((a+2), (b+5), c));
	printf("3. c = %d+2 * %d+5 :%d\n", a, b, GET_PRODUCT(a+2, b+5, c));
	printf("%d\n", (c =  a + 2 * b + 5));
	printf ("hello world\n");

}

// 2 + 5 + 4
// 2 * 5 + 4
