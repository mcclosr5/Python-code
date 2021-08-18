#!/usr/bin/env python

import sys

s = sys.stdin.read()
i = 0
count = 0

while i < len(s):
	if ('0' <= (s[i]) and (s[i]) <= '9'):
		count = count + 1
	i += 1

print count
