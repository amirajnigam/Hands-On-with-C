#include <stdio.h>

int main()
{

    int pizzaToEat = 100;
    printf("pizzaToEat:%i\n", pizzaToEat);
    pizzaToEat +=100;
    printf("pizzaToEat: %i\n", pizzaToEat);
    pizzaToEat -=100; //100
    pizzaToEat *=2; // 200
    pizzaToEat /=4; //50
    pizzaToEat %=5; // 0
    printf("pizzaToEat : %i\n", pizzaToEat);
}
