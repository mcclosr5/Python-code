#!/usr/bin/env python

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

i = 0
while i < len(a) / 2:
	swap(a, i, len(a) - i - 1)
	i += 1
print a
