#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch; 
    char s[100]; 
    char s1[100];

    scanf("%c%*c", &ch);  //So, the statement: scanf("%[^\n]%*c", s); will not work because the last statement will read a newline character from the previous line.
                          // This can be handled in a variety of ways and one of them being: scanf("\n"); before the last statement.
    scanf("%s%*c", &s);   
    scanf("%[^\n]",&s1);
    printf("%c\n", ch);    
    printf("%s\n", s);
    printf("%s", s1); 
    return 0;
}