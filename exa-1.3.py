#!/usr/bin/env python

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as fd:
	s = fd.readlines()
if len(s) > 0:
	print 'non-empty'
else:
    print 'empty'
