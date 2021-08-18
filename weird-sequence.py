#!/usr/bin/env python

s = input()
i = 0
while i < s:
	if i % 2 != 0:
		print i - (i * 2)
	else:
		print i
	i += 1
