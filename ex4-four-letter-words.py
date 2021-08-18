#!/usr/bin/env python

import sys

s = sys.stdin.read()
i = 0
s = s.split(' ')
while i < len(s):
	if len(s[i]) == '4':
		s[i] == '****'
	print s[i]
	i += 1
    