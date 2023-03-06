#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
#include <string.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	slow_ptr = list->next;
	fast_ptr = (list->next)->next;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		if (slow_ptr != fast_ptr)
		{
			slow_ptr = slow_ptr->next;
			fast_ptr = (fast_ptr->next)->next;
		}
		else
			return (1);
	}
	return (0);
}
