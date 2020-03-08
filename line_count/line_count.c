#include<stdio.h>

void main()
{
	int n,c;

	n = 0;
	while( (c = getchar()) != '\0')
	{
		if( c == '\n')
		++n;
	printf("%d\n", n);
	}
}
