#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: list
 * Return: 1 if theres cycle, 0 if theres not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
