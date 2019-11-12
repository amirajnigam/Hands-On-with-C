#include<stdio.h>
int main()
{

int radius;
printf("Please enter a radius:");
scanf("%i", &radius);
double area = 3.14 * radius*radius;
printf("The area of circle with %i radius is %f\n", radius, area);
}
