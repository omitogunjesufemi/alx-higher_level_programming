#include "lists.h"

/**
 * insert_node - Inserts a node to a sorted singly linked list
 * @head: The pointer to the first node
 * @number: the number of the node to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *current;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head != NULL)
	{
		current = *head;
		while (number > current->n)
		{
			prev = current;
			current = current->next;
		}
		prev->next = new_node;
		new_node->next = current;
		return (new_node);
	}
	new_node->next = *head;
	return (new_node);
}
