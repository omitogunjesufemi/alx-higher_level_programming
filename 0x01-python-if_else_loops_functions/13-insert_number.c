#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list
 * @head: The beginning of the node
 * @number: The number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prv_ptr, *curr_ptr, *new;

	curr_ptr = *head;
	prv_ptr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (curr_ptr != NULL)
		{
			if (curr_ptr->n > number)
			{
				new->next = curr_ptr;
				prv_ptr->next = new;
				return (new);
			}
			prv_ptr = curr_ptr;
			curr_ptr = curr_ptr->next;
		}
	}
	return (new);
}
