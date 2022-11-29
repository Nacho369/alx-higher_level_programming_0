#include "lists.h"

/**
 * check_cycle -  Checks if a singly linked list has a
 * cycle in it.
 *
 * @list: Pointer tot the list
 *
 * Return: 0 - if no cycle; 1 - if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *temp = list;

	while (
	temp != NULL && ptr->next != NULL && ptr->next->next != NULL
	)
	{
		ptr = ptr->next->next;
		temp = temp->next;

		if (ptr == temp)
			return (1);
	}

	return (0);
}
