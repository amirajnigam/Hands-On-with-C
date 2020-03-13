#include<unistd.h>
#include<stdio.h>
#include<string.h>

void	uppercase( char str[])
{
	int i; 

	i = 0;
	while(str[i])
	{
		str[i] = str[i] - 32;
		//write(1, str[i], 1);
		++i;
	}		
	write(1, str, strlen(str));
}

int	main(int argc,char **argv)
{
	if(argc  == 2)
	{
		uppercase(argv[1]);
	}
	write(1, "\n", 1);
	return(0);
}

