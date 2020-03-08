#include <stdio.h>

int main()
{
    long nc;

    for( nc = 0; getchar() != '\0'; ++nc)
    printf("%ld\n", nc);
    return (0);
}
