#!/usr/bin/env python

import sys

def first_odd_position(a):
	i = 0
	while i < len(a):
		if int(a[i]) % 2 != 0:
			return i
		i += 1