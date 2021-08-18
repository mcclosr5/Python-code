#!/usr/bin/env python

import sys

s = sys.stdin.read()
cap = 0
i = 0

while i < len(s):
	if ('A' <= s[i] and s[i] <= 'Z'):
		cap = cap + 1
	i += 1

print cap
