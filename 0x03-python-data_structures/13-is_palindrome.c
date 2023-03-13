#include "lists.h"

listint_t *get_end_ptr(listint_t *head_ptr);
listint_t *move_end_ptr(listint_t *end_ptr, listint_t *moving_ptr);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start_ptr, *end_ptr;

	if (*head == NULL)
		return (1); /* An empty list is considered a palindrome */

	start_ptr = *head;
	end_ptr = get_end_ptr(start_ptr);

	while (start_ptr->next != end_ptr)
	{
		if (start_ptr->n != end_ptr->n)
		{
			return (0);
		}
		end_ptr = move_end_ptr(end_ptr, start_ptr);
		start_ptr = start_ptr->next;
	}

	return (1);

}

/**
 * get_end_ptr - Get to the end of a linked list
 * @head_ptr: Pointer to head of list
 * Return: Pointer to the last node on the list
 */
listint_t *get_end_ptr(listint_t *head_ptr)
{
	while (head_ptr->next != NULL)
		head_ptr = head_ptr->next;

	return (head_ptr);
}

/**
 * move_end_ptr - Get to the node before the end of a linked list
 * @end_ptr: Pointer to end of list
 * @moving_ptr: Moving pointer of list
 * Return: Pointer to the node before last node on the list
 */
listint_t *move_end_ptr(listint_t *end_ptr, listint_t *moving_ptr)
{
	while (moving_ptr->next != end_ptr)
		moving_ptr = moving_ptr->next;

	return moving_ptr;
}
