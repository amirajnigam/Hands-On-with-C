#include<stdio.h>
#define MAXLINE	1000

int	getlen(char s[], int lim);
void	copy(char to[], char from[]);

int main()
{
	int len;
	int max;
	char line[MAXLINE];
	char longest[MAXLINE];

	max = 0;
	while((len = getlen(line, MAXLINE)) > 0)
	{
		if (len > max)
		{
			max = len;
			copy(longest, line);
		}
	}
		if (max > 0)
		printf("%s", longest);
	return (0);
}

int getlen(char s[], int lim)
{
	int i, c;
	
	for(i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i)
		s[i] = c;
	if(c == '\n')
	{
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	return i;
}

void copy(char to[], char from[])
{
	int i;

	i = 0;
	while(from[i])
	{
		to[i] = from[i];
		++i;
	}	
}
