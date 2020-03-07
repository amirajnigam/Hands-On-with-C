#include <stdio.h>

int max_of_four(int a, int b, int c, int d)
{
    int x, y;

    if (a > b)
        x = a;
    else
        x = b;
    
    if ( c > d)
        y = c;
    else 
        y = d;
    if ( x > y)
        return (x);
    else 
        return (y);
}

int main()
{
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}