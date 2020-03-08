#include<stdio.h>

#define	IN	1
#define	OUT	0

void main()
{
	int c, nl, nw, nc, state;

	state = OUT;   //state = 0
	nl = nw = nc = 0;
	while( (c = getchar()) != '\0')
	{
		++nc;
		if ( c == '\n')
			++nl;
		if ( c == ' ' || c == '\n' || c == '\t')
			state = OUT;
		else if (state == OUT)
		{
			state = IN;
			++nw;
		}
	}
	printf("%d %d %d\n", nl, nw, nc);
}
