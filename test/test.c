#include<stdio.h>

int global = 10;    //uninitialized variable stored in DS

int main(void)
{
	static int i = 100; //uninitialized static variable stored in DS

	return (0);
}
