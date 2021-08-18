#!/usr/bin/env python3

def even_count(lst):
	count = 0
	pointer = lst.head
	while pointer != None:
		if pointer.item % 2 == 0:
			count = count + 1
		pointer = pointer.next
	return count
