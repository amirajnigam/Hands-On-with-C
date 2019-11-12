#include <stdio.h>
int main()
{
    int eggs;
    printf("Enter the number of eggs:");
    scanf("%i", &eggs);

    double dozen =  eggs/12.0;
    printf("You have %f dozen eggs.\n", dozen);
}
