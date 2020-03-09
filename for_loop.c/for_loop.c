#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

int a, b;
char *strings[] = {"one", "two", "three", "four", "five", "six", "seven",  "eight",     "nine", "even", "odd"};

scanf("%d\n%d", &a, &b); // 8,11 
int labels_index;
for (int i=a; i<=b; i++) // ( i = 8, i <= 11, i++); i = 8,9,10,11
{    
	if (i <= 9) 
	printf ("%s\n", strings[i-1]); // strings[7],8,9, 10  
	else 
	printf ("%s\n", strings[9+(i%2)]);
}
return 0;
}
