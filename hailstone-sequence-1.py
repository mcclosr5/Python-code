#!/usr/bin/env python

s = input()
r = input()
i = 0
while i < s:
	print r
	if r % 2 != 0:
		r = (r * 3) + 1

	else:
	    r = r / 2
	i += 1
