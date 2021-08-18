#!/usr/bin/env python

import sys

word = sys.argv[1]

if len(word) % 2 == 0:
	print(word[len(word) // 2:])

else:
	print(word[0] + word[len(word) - 1])
