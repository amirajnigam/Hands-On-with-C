#include<stdio.h>
#include<stdlib.h>
#define CAPACITY 5

int stack[CAPACITY], top = -1;
void push(int);
int isfull(void);
int pop(void);
int isempty(void);
void peak(void);
void traverse(void);
void main(void)
{
	int ch, item;
	
	while(1)
	{
		printf("1.Push \n");
		printf("2.Pop \n");
		printf("3.Peak \n");
	        printf("4.Traverse \n");
		printf("5.Quit \n");	
		printf("Enter the choice:\n");
		scanf("%d", &ch);
		switch(ch)
		{
			case 1 : printf("Enter the element:\n");
				 scanf("%d", &item);
			 	 push(item);
			 	 break;
			case 2 : item = pop();
				 if(item = 0)
					 printf("Stack Underflow\n");
			 	 else
					 printf(" Popped Item:%d\n", item);
			 	 break;
			case 3 : peak();
				 break;
			case 4 : traverse();
			 	 break;
			case 5 : exit(0);
			default: printf("Invalid Input\n");
		}
	}	
	void pusih( int ele)
	{
		if(isfull())
			printf("Stack overflow\n");
		else
		{
			top++;
			stack[top] = ele;
			printf("Element Inserted\n");
		}
	}
	int isfull()
	{
		if(top == (CAPACITY - 1))
			return (1);
		else
			return (0);
	}
	int pop()
	{
		if(isempty())
			return (0);
		else
		{
			return (stack[top--]);
		}
	}
	int isempty()
	{
		if(top == -1)
			return (1);
		else 
			return (0);
	}

	void peak()
	{
		if(isempty())
			printf("Stack is Empty\n");
		else
			printf("top element : %d \n", stack[top]);
	}
	
	int traverse()
	{
		if(isempty())
			printf("Stack is Empty \n");
		else
		{
			for(int i = 0; i <= top; ++i)
				printf("Elements list: %d \n", stack[i]);
	 	}
 	}
}
