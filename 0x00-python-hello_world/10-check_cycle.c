#include "lists.h"

/**
 * check_cycle - function that checks for a loop in a LL
 * @list: head of the linked list
 *
 * Return: 1 if cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
