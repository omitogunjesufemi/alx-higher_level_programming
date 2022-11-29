#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Singly linked list
 * Return: o if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;
	int flag;

	flag = 0;
	if (list == NULL)
		return (flag);
	if (list->next != NULL)
	{
		slow_ptr = list->next;
		fast_ptr = (list->next)->next;

		while (fast_ptr != NULL)
		{
			if (slow_ptr == fast_ptr)
			{
				flag = 1;
				return (flag);
			}
			slow_ptr = slow_ptr->next;
			fast_ptr = (fast_ptr->next)->next;
		}
		return (flag);
	}
	return (flag);
}
