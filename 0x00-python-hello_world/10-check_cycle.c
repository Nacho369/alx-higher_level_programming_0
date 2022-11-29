#include "lists.h"

int check_cycle(listint_t *list)
{
	int node;
	listint_t *ptr = list;

	if (list == NULL)
		return (1);
	else
	{
		for (node = 0; ptr->next != NULL; node++)
			ptr = ptr->next;

		if (ptr->next == NULL)
			return (0);
	}
	return (1);
}
