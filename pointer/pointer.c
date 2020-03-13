#include<stdio.h>

void increment(int *v)
{
	(*v)++;
}





int	main(void)
{
	int a;
	
	printf("Enter a number:");
	scanf("%d", &a);
	increment(&a);
	printf("%d\n", a);
	return (0);
}
