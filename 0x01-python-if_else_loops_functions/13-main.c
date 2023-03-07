#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 10);
    add_nodeint_end(&head, 11);
    add_nodeint_end(&head, 12);
    add_nodeint_end(&head, 13);
    add_nodeint_end(&head, 14);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 8000);

    print_listint(head);

    free_listint(head);

    return (0);
}
