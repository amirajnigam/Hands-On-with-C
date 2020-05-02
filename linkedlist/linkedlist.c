#include<stdio.h>
#include<stdlib.h>

struct node
{
		int data;
			struct node* next;
};

void	printlist(struct node* n)
{
		while(n != NULL)
				{
							printf("%d", n-> data);
									n = n-> next;
										}
			putchar('\n');
}

int main()
{
		struct node* first = NULL;
			struct node* second = NULL;
				struct node* third = NULL;

					first = (struct node*)malloc(sizeof(struct node));
						second = (struct node*)malloc(sizeof(struct node));
							third = (struct node*)malloc(sizeof(struct node));

								first->data = 1;
									first->next = second;

										second->data = 2;
											second->next = third;

												third->data = 3;
													third->next = NULL;

														printlist(first);
															return (0);
}
