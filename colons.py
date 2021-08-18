#!/usr/bin/env python

import sys

args = sys.argv[1:]

empty = ''
for words in args:
	empty = empty + ':' + words
print(empty + ':')
