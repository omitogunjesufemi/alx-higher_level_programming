#include "lists.h"

listint_t *end_node(listint_t *start, int *total_node);
listint_t *shift_end_node(listint_t *start, listint_t *end);

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if it is not a palindrome, 1 of it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	int total_node;

	if (*head != NULL)
	{
		start = *head;
		end = end_node(start, &total_node);
		if (total_node % 2 != 0)
		{
			while (start != end)
			{
				if (start->n != end->n)
					return (0);
				start = start->next;
				end = shift_end_node(start, end);
			}
		}
		else
		{
			if (start->n != end->n)
				return (0);
			while (start->next != end)
			{
				if (start->n != end->n)
					return (0);
				start = start->next;
				end = shift_end_node(start, end);
			}
		}
		return (1);
	}
	return (1);
}

/**
 * shift_end_node - Shift the end node a step backward
 * @start: The starting point
 * @end: The ending point
 * Return: the pointer to end node
 */
listint_t *shift_end_node(listint_t *start, listint_t *end)
{
	while (start->next != end)
	{
		start = start->next;
	}
	return (start);
}

/**
 * end_node - Shift the end node a step backward
 * @start: The starting point
 * Return: the pointer to end node
 */
listint_t *end_node(listint_t *start, int *total_node)
{
	int i;

	i = 1;
	while (start->next != NULL)
	{
		start = start->next;
		i++;
	}
	*total_node = i;
	return (start);
}
